# Automationsdefinitioner

Katalogen innehåller versionshanterade kopior av de aktiva Codex-automationerna som producerar rapporterna i repot.

## Omfattning

- `readwise-cybersecurity-report`
- `readwise-threat-intelligence-report`
- `readwise-generative-ai-report`
- `readwise-cybersecurity-notebooklm-digest`

Varje underkatalog innehåller automationens `automation.toml`. Filerna inkluderar prompt, schema, modell, körmiljö och workspace-rötter. De kan innehålla lokala projekt-ID:n och absoluta sökvägar och är därför en återställningskälla, inte en portabel installationsmekanism.

Runtime-minne, körhistorik och autentiseringsdata versionshanteras inte.

## Synkronisering

Kontrollera om de lokala definitionerna skiljer sig från repot:

```bash
scripts/automations/sync.sh check
```

Exportera aktuella definitioner från Codex till repot:

```bash
scripts/automations/sync.sh export
```

Granska alltid diffen innan commit. Återställning till Codex görs via desktopappens automationer efter kontroll av projekt-ID, sökvägar och behörigheter.
