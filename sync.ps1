<#
.SYNOPSIS
  Sincroniza o Time Chaves a partir do repositorio oficial para o global e o Drive.
.DESCRIPTION
  Fonte da verdade: este repositorio (C:\Users\mgara\repos\time-chaves-opencode).
  Destinos:
    1) Global do OpenCode  -> ~/.config/opencode  (o que roda em qualquer projeto)
    2) Copia no Google Drive (espelho, sem Git)
  Opcionalmente commita e faz push no GitHub.
.PARAMETER SkipGlobal
  Nao sincroniza para o global.
.PARAMETER SkipDrive
  Nao sincroniza para o Drive.
.PARAMETER NoGit
  Nao faz commit/push.
.PARAMETER Message
  Mensagem de commit. Padrao: "sync: atualiza Time Chaves".
.EXAMPLE
  .\sync.ps1
  .\sync.ps1 -Message "novo agente roberto"
  .\sync.ps1 -SkipDrive
#>
[CmdletBinding()]
param(
  [switch]$SkipGlobal,
  [switch]$SkipDrive,
  [switch]$NoGit,
  [string]$Message = "sync: atualiza Time Chaves"
)

$ErrorActionPreference = 'Stop'

# --- Caminhos ---
$Repo     = $PSScriptRoot
$GlobalCfg = Join-Path $env:USERPROFILE ".config\opencode"
$Drive     = "G:\Meu Drive\Time do Chaves\Time do Chaves Open code"

function Info($m) { Write-Host "  $m" -ForegroundColor Cyan }
function Ok($m)   { Write-Host "  [OK] $m" -ForegroundColor Green }
function Warn($m) { Write-Host "  [!] $m" -ForegroundColor Yellow }

Write-Host "`n=== Sync Time Chaves ===" -ForegroundColor White
Info "Repo: $Repo"

if (-not (Test-Path (Join-Path $Repo "opencode.jsonc"))) {
  throw "Nao encontrei a raiz do repo em '$Repo' (opencode.jsonc ausente). Rode dentro do repo oficial."
}

# --- 1) Sincroniza para o GLOBAL ---
if (-not $SkipGlobal) {
  Write-Host "`n[1/3] Global do OpenCode" -ForegroundColor White
  $pairs = @(
    @{ Src = Join-Path $Repo ".opencode\agents";   Dst = Join-Path $GlobalCfg "agents" },
    @{ Src = Join-Path $Repo ".opencode\skills";   Dst = Join-Path $GlobalCfg "skills" },
    @{ Src = Join-Path $Repo ".opencode\commands"; Dst = Join-Path $GlobalCfg "commands" }
  )
  foreach ($p in $pairs) {
    if (-not (Test-Path $p.Src)) { Warn "origem ausente: $($p.Src)"; continue }
    New-Item -ItemType Directory -Path $p.Dst -Force | Out-Null
    # /E copia subpastas; SEM /PURGE para nao apagar itens globais que nao sejam do time
    # /XF desktop.ini evita poluir o global com lixo do Windows/Drive
    robocopy $p.Src $p.Dst /E /COPY:DAT /XF "desktop.ini" "Thumbs.db" /NFL /NDL /NJH /NJS /NP | Out-Null
    Ok "$($p.Src) -> $($p.Dst)"
  }
} else { Warn "global ignorado (-SkipGlobal)" }

# --- 2) Sincroniza para o DRIVE ---
if (-not $SkipDrive) {
  Write-Host "`n[2/3] Copia no Google Drive" -ForegroundColor White
  if (-not (Test-Path "G:\")) {
    Warn "Drive G: nao esta montado. Abra o Google Drive e rode de novo. (pulei)"
  } else {
    if (-not (Test-Path $Drive)) { Warn "pasta do Drive ausente: $Drive (pulei)" }
    else {
      $sw = [Diagnostics.Stopwatch]::StartNew()
      # Espelha o conteudo do repo, exceto artefatos de Git e do proprio Drive
      robocopy $Repo $Drive /E /COPY:DAT /XD ".git" ".opencode\.git" /XF ".gitignore" "desktop.ini" `
        /NFL /NDL /NJH /NJS /NP | Out-Null
      $sw.Stop()
      Ok "espelho atualizado ($([math]::Round($sw.Elapsed.TotalSeconds,1))s)"
    }
  }
} else { Warn "Drive ignorado (-SkipDrive)" }

# --- 3) Git: commit + push ---
if (-not $NoGit) {
  Write-Host "`n[3/3] Git (commit + push)" -ForegroundColor White
  Push-Location $Repo
  try {
    $dirty = git status --porcelain
    if (-not $dirty) {
      Ok "sem mudancas para commitar"
    } else {
      git add -A
      git -c core.safecrlf=false commit -m $Message | Out-Null
      Ok "commit: $Message"
    }
    git push 2>&1 | ForEach-Object { $_ }
    Ok "push concluido"
  } finally { Pop-Location }
} else { Warn "git ignorado (-NoGit)" }

Write-Host "`n=== Fim ===" -ForegroundColor White
