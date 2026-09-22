# Cybersecurity Report — 2026-06-15

## Week in Security
This week’s reporting was dominated by initial-access and credential-theft chains rather than classic perimeter malware alone: a live PeopleSoft zero-day, repeat software supply-chain compromises, and social engineering campaigns built around AI brands all pointed to trust abuse as the main theme. Defenders also kept moving controls closer to the point of abuse, with new Exchange audit telemetry for hidden mailbox copy activity and more runtime controls for local AI agents, CI/CD workflows, and cloud app governance. AI security remained tightly coupled to mainstream enterprise security rather than a separate domain, showing up in prompt-injection, agent runtime, model governance, and phishing coverage. The underlying Reader collection is still stale beyond the current `later` slice: after the recent June material, both `feed` and much of the tagged backlog fall back quickly into 2025-2023 content, which is a tagging hygiene problem rather than evidence of a quiet threat week.

## Notable Incidents & Breaches
Oracle PeopleSoft became one of the week’s most important incidents after ShinyHunters exploited CVE-2026-35273, a remotely exploitable SSRF rated 9.8, against roughly 100 organizations and about 300 endpoints. Higher education was hit hardest, and the University of Nottingham confirmed a significant data compromise. The lesson is straightforward: internet-facing enterprise applications with delayed patch coverage need compensating controls, rapid vendor advisory monitoring, and aggressive outbound-connection review because attackers were already staging and exfiltrating data before Oracle issued guidance.

Dashlane disclosed that attackers obtained encrypted vault copies from fewer than 20 customer accounts by brute-forcing device-registration workflows at scale rather than attacking one account at a time. The direct impact appears limited, but the incident showed how MFA-adjacent enrollment flows can become a concentration point for abuse when registration tokens, lockouts, and notification patterns are not resilient to spraying tactics. Organizations should review every “add device” or recovery workflow with the same scrutiny applied to primary login.

Researchers also showed that a Creative Sound Blaster Katana V2X speaker could be turned into a Bluetooth-range attack path against a USB-connected PC by flashing malicious firmware and abusing HID behavior. The practical exposure is proximity-limited, but it is a useful reminder that peripheral trust assumptions remain weak, especially where firmware signing and pairing controls are missing.

## Vulnerabilities & Patches
The highest-priority vulnerability in this week’s set was CVE-2026-35273 in PeopleSoft. Mandiant linked exploitation to extortion activity, Oracle acknowledged the issue, and the combination of active exploitation, high severity, and real victim disclosures puts it firmly in emergency-response territory.

Linux defenders also had to account for CVE-2026-23111, a high-severity nf_tables privilege-escalation bug caused by a single logic error that can let an unprivileged user gain root. The exploitability matters because local privilege escalation remains a reliable second-stage move after initial compromise, especially on shared systems and container hosts.

Microsoft’s June fixes included CVE-2026-45586, a Windows local privilege-escalation zero-day disclosed publicly before patching. Separately, the week reinforced that patching the application alone is not enough: unsupported runtime dependencies such as end-of-life Visual C++ and .NET components remain an overlooked attack surface even when the parent application appears current.

## Threat Actor Activity
ShinyHunters was the clearest named actor in this week’s reporting, using the PeopleSoft flaw for broad exploitation, data theft, and extortion. The group’s targeting of higher education fits its history of opportunistic, high-volume compromise combined with downstream monetization through leak pressure.

Microsoft also tied multiple AI-themed lures to active criminal operations. Storm-3075 used fake AI tools and malvertising to deliver payloads including Vidar, while Fox Tempest provided malware-signing support that made those binaries look more legitimate. In parallel, TeamPCP-linked Miasma activity showed how threat actors are adapting supply-chain attacks to AI-assisted developer workflows by stealing cloud and publishing credentials, reusing trusted OIDC flows, and moving laterally through package ecosystems.

## Cloud & Identity Security
Exchange Online added a useful new signal by logging `CopyFromIPM` events when mail is copied from the user-visible mailbox tree into the hidden non-IPM subtree. That closes an audit gap relevant to mailbox data staging and exfiltration, and defenders should add the new event type to hunting and detection content immediately.

Identity and agent security also converged this week. Microsoft’s CI/CD research on Anthropic’s Claude Code GitHub Action showed how prompt injection against untrusted issue or pull-request content could expose runner secrets when file-read controls were weaker than subprocess sandboxing. The broader lesson is that any agent processing untrusted repository content must be treated as high risk if it can read files, access secrets, or communicate externally.

Local AI agents were another recurring concern. Microsoft’s new coverage around local agents, runtime isolation, data-loss prevention, and network enforcement reflects a real change in the attack surface: agents now inherit endpoint context, tokens, and user data directly, so endpoint, identity, and data-security teams need shared controls rather than separate AI-only processes.

## Recommended Actions
1. Treat PeopleSoft exposure as urgent: apply Oracle mitigations immediately, hunt for related IOCs, and review outbound SSH and archive activity from PeopleSoft and WebLogic infrastructure.
2. Review identity workflows that sit next to primary authentication, especially device enrollment, recovery, and token issuance paths; rate-limit them, add anomaly detection, and test them against spraying scenarios.
3. Hunt for supply-chain blast radius from Microsoft and Red Hat package compromise reporting; rotate developer, CI/CD, cloud, and package-publishing credentials where affected packages or workflows were touched.
4. Add detections for Exchange `CopyFromIPM` activity and review mailbox auditing coverage for hidden-folder staging and exfiltration patterns.
5. Reassess any AI agent or CI workflow that processes untrusted content while holding secrets or write-capable tools; enforce least privilege, isolate runtime access, and block sensitive file paths by default.
6. Start an inventory of unsupported runtimes and peripheral firmware trust gaps; these are lower-profile issues than zero-days, but they create durable exploit paths that attackers continue to reuse.

## Sources
- PeopleSoft 0-day affecting hundreds of organizations steals gigabytes of data — https://arstechnica.com/security/2026/06/peoplesoft-0-day-affecting-hundreds-of-organizations-steals-gigabytes-of-data/
- New Exchange Online Mailbox Auditing Signal: Visibility into IPM to Non-IPM Copy Activity — https://techcommunity.microsoft.com/t5/microsoft-security-community/new-exchange-online-mailbox-auditing-signal-visibility-into-ipm/ba-p/4526914
- Locked in heated rivalry with researcher, Microsoft fixes 0-day they disclosed — https://arstechnica.com/security/2026/06/locked-in-heated-rivalry-with-researcher-microsoft-fixes-0-day-they-disclosed/
- High-severity vulnerability in Linux caused by a single errant character — https://arstechnica.com/security/2026/06/a-single-errant-character-in-the-linux-kernel-allows-attacker-to-gain-root/
- For the 2nd time in weeks, Microsoft packages laced with credential stealer — https://arstechnica.com/security/2026/06/for-the-2nd-time-in-weeks-microsoft-packages-laced-with-credential-stealer/
- AI brands as bait: How threat actors are using the AI hype in social engineering — https://www.microsoft.com/en-us/security/blog/2026/06/08/ai-brands-as-bait-how-threat-actors-are-using-the-ai-hype-in-social-engineering/
- Dashlane explains how attackers managed to download encrypted password vaults — https://arstechnica.com/security/2026/06/dashlane-explains-how-attackers-managed-to-download-encrypted-password-vaults/
- Dashlane issues opaque advisory warning 20 encrypted vaults were stolen — https://arstechnica.com/security/2026/06/dashlane-issues-opaque-advisory-warning-20-encrypted-vaults-were-stolen/
- How a USB-connected speaker can infect a PC without ever being touched — https://arstechnica.com/security/2026/06/highly-reviewed-speaker-can-be-hacked-over-the-air-to-infect-connected-devices/
- Securing CI/CD in an agentic world: Claude Code Github action case — https://www.microsoft.com/en-us/security/blog/2026/06/05/securing-ci-cd-in-agentic-world-claude-code-github-action-case/
- Preinstall to persistence: Inside the Red Hat npm Miasma credential-stealing campaign — https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/
- Reconstructing AI activity in investigations — https://www.microsoft.com/en-us/security/blog/2026/06/09/reconstructing-ai-activity-investigations/
- Disable alert generation for Unsanctioned Apps in Microsoft Defender for Cloud Apps — https://jeffreyappel.nl/disable-alert-generation-for-unsanctioned-apps-in-microsoft-defender-for-cloud-apps/
- Your Apps Are Running on Borrowed Time: The Hidden Risk of Out-of-Support Runtime Dependencies — https://msendpointmgr.com/2026/06/04/your-apps-are-running-on-borrowed-time-the-hidden-risk-of-out-of-support-runtime-dependencies/
- Microsoft Build 2026: Securing code, agents, and models across the development lifecycle — https://www.microsoft.com/en-us/security/blog/2026/06/02/microsoft-build-2026-securing-code-agents-and-models-across-the-development-lifecycle/
- Securing the new risk surface: local agents, claws, and open runtimes — https://techcommunity.microsoft.com/t5/microsoft-security-community/securing-the-new-risk-surface-local-agents-claws-and-open/ba-p/4524602
