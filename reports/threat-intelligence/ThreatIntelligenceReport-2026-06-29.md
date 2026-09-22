# Threat Intelligence Report — 2026-06-29

## Executive Summary
Current Microsoft 365 and Azure risk is concentrated in three areas: infostealer-driven identity compromise, AiTM phishing that aims at Microsoft sign-in flows and tokens, and software supply-chain attacks that target developer and CI/CD credentials with Azure and cloud metadata theft in scope. The most urgent threat is the continued use of stealers and commodity loaders to harvest session cookies, SSO tokens, and cloud credentials that can bypass MFA and turn unmanaged-device compromise into tenant compromise.

The `threat intelligence` collection is stale for this scope. The merged `later` and `feed` pool contains 333 unique tagged documents, but much of the pool is older or outside Microsoft 365, Entra ID, Azure, BEC, phishing, ransomware, or AiTM relevance. This report therefore focuses on the current identity and cloud threats supported by the latest in-scope material.

## Key Threats

### StealC and Amadey enable MFA-bypassing identity compromise
**Type:** Infostealer and malware delivery service
**Severity:** Critical
**MITRE ATT&CK:** T1555, T1115, T1113, T1090, T1053.005, T1048.002
**CVEs:** None
**Affected:** Windows endpoints, browsers, Outlook profiles, enterprise VPN and SSO credentials
**M365/Azure relevance:** Stolen browser cookies, Outlook credentials, and SSO artifacts can be used against Microsoft 365 and Entra-backed applications without triggering traditional password-reset defenses.
**Summary:** Microsoft documented StealC as an infostealer sold as a service and Amadey as a loader used to deliver it. The pair harvests passwords, cookies, Outlook account data, files, and host telemetry, then feeds an access-broker ecosystem that can hand working enterprise access to ransomware and follow-on intrusion teams.
**Recommendations:** Reset sessions for exposed users and enforce reauthentication. Expand detections for infostealer-to-identity abuse across unmanaged devices, browsers, and VPN access. Tighten token protection, conditional access, and device-based access controls for privileged roles.
**Source:** StealC and Amadey: Breaking down infostealers and the cybercrime services that deliver them — https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/

### Parallel threat activity raises the chance of hybrid identity persistence
**Type:** Multi-actor intrusion and post-compromise persistence
**Severity:** High
**MITRE ATT&CK:** T1190, T1219, T1572, T1098, T1574.002
**CVEs:** None specified
**Affected:** On-premises SharePoint, hybrid identities, domain administration paths, remote access channels
**M365/Azure relevance:** Hybrid Microsoft estates remain exposed when on-premises compromise is used to pivot into cloud identities, trusted admin tools, and persistent access paths that blend with legitimate operations.
**Summary:** Microsoft DART reported an intrusion where Storm-2603 and a second unrelated actor operated in parallel. The case combined SharePoint exploitation, Cloudflare tunneling, Zoho Assist, SSH through Visual Studio Code, new admin accounts, and DLL sideloading, making attribution and response materially harder.
**Recommendations:** Patch internet-facing Microsoft workloads aggressively, especially hybrid entry points. Restrict and monitor tunneling, remote-admin, and developer tools in production estates. Correlate endpoint, identity, and cloud telemetry so separate activity clusters are not treated as one incident.
**Source:** One intrusion, two cyberattackers: Uncovering parallel threat activity — https://www.microsoft.com/en-us/security/blog/2026/06/22/one-intrusion-two-cyberattackers-uncovering-parallel-threat-activity/

### AI-brand phishing is being used to drive AiTM and BEC access theft
**Type:** Phishing, AiTM, and social engineering
**Severity:** Critical
**MITRE ATT&CK:** T1566.001, T1566.002, T1550.004
**CVEs:** None
**Affected:** Email users, Microsoft sign-in flows, browser sessions, enterprise identities
**M365/Azure relevance:** Microsoft observed Claude-themed infrastructure consistent with a final-stage Microsoft sign-in theft flow, along with broader AI-brand lures that can lead to token interception, account takeover, and BEC.
**Summary:** Microsoft tracked multiple campaigns abusing ChatGPT, Claude, DeepSeek, Copilot, and other AI brands. The most relevant cluster used Anthropic-themed lures and staging pages that strongly indicated a final Microsoft sign-in page designed for AiTM-style token interception. Microsoft also tied related malvertising to Storm-3075 and malware-signing support from Fox Tempest.
**Recommendations:** Require phishing-resistant MFA for admins and high-risk users. Recheck all email links at click time and monitor for token anomalies, unfamiliar sign-in properties, and session-cookie abuse. Train users to treat AI account-policy messages and download prompts as hostile by default.
**Source:** AI brands as bait: How threat actors are using the AI hype in social engineering — https://www.microsoft.com/en-us/security/blog/2026/06/08/ai-brands-as-bait-how-threat-actors-are-using-the-ai-hype-in-social-engineering/

### Exchange Online mail-copy evasion now has a visible audit trail
**Type:** Mailbox data staging and exfiltration evasion
**Severity:** High
**MITRE ATT&CK:** T1114.001
**CVEs:** None
**Affected:** Exchange Online mailboxes and Unified Audit Log workflows
**M365/Azure relevance:** This is a direct Exchange Online abuse path: attackers can copy visible mailbox content into the hidden non-IPM subtree before exfiltration, reducing forensic visibility if defenders are not watching for the new signal.
**Summary:** Microsoft disclosed a previously weakly instrumented technique where mail items are copied from visible IPM folders into the hidden non-IPM subtree before exfiltration. Exchange Online now emits a `MailItemsAccessed` event with `AccessType=CopyFromIPM`, closing a gap seen in real investigations.
**Recommendations:** Add detections and hunting for `CopyFromIPM` immediately. Review historical mailbox investigations for non-IPM abuse and hidden-folder staging. Pair mailbox auditing with incident playbooks for BEC, insider misuse, and post-compromise collection.
**Source:** New Exchange Online Mailbox Auditing Signal: Visibility into IPM to Non-IPM Copy Activity — https://techcommunity.microsoft.com/t5/microsoft-security-community/new-exchange-online-mailbox-auditing-signal-visibility-into-ipm/ba-p/4526914

### The Miasma campaign shows how npm compromise can become Azure credential theft
**Type:** Software supply-chain compromise
**Severity:** Critical
**MITRE ATT&CK:** T1195.001, T1552, T1528
**CVEs:** None
**Affected:** npm ecosystems, developer workstations, GitHub Actions, Azure IMDS tokens, Entra/Graph access paths, Key Vault
**M365/Azure relevance:** Microsoft’s Red Hat campaign analysis explicitly documented theft of Azure metadata tokens for `management.azure.com`, `graph.microsoft.com`, and Key Vault resources, creating a direct path from package install to Azure control-plane access.
**Summary:** The Red Hat npm compromise embedded a credential-stealing payload that abused trusted publishing and valid provenance while targeting GitHub, npm, AWS, Azure, GCP, Vault, and Kubernetes secrets. The malware also scraped CI runner memory, republished poisoned packages, and attempted to persist and spread across maintainers and build systems.
**Recommendations:** Rotate Azure, Graph, Key Vault, GitHub, npm, and CI/CD credentials from any exposed runner or developer host. Disable install scripts where feasible and pin known-good package versions. Hunt for unusual token acquisition from metadata endpoints and for Node-to-Bun execution chains in build environments.
**Source:** Preinstall to persistence: Inside the Red Hat npm Miasma credential-stealing campaign — https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/

### Dependency-confusion packages are profiling developer environments for later cloud abuse
**Type:** Dependency confusion and staged developer compromise
**Severity:** High
**MITRE ATT&CK:** T1195.001, T1592, T1082
**CVEs:** None
**Affected:** Internal package namespaces, developer hosts, CI/CD runners, cloud and token-bearing environments
**M365/Azure relevance:** While this campaign was in reconnaissance mode, it targeted internal package ecosystems and developer contexts that often hold Azure credentials, Microsoft tenant tokens, and CI secrets needed for later Microsoft cloud intrusion.
**Summary:** Microsoft found malicious npm packages published under lookalike organizational scopes to win dependency resolution and silently install an obfuscated recon payload. The actor used shared C2 infrastructure, staged high version numbers, fake internal metadata, and a `RECON_ONLY` model that can be toggled into full exploitation later.
**Recommendations:** Scope-lock internal package names to private registries and prevent fallback to public npm. Audit developer and runner systems for dropped payloads, odd cache markers, and outbound traffic to campaign infrastructure. Treat package-resolution mistakes as credential exposure, not just build hygiene issues.
**Source:** Malicious npm packages abuse dependency confusion to profile developer environments — https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/

## Threat Actor Activity
Storm-2603 appeared in hybrid intrusion activity that overlapped with a second actor in the same environment, reinforcing the need to expect multi-actor access on the same victim. Storm-3075 and Fox Tempest remain relevant to Microsoft customers because AI-themed malvertising and code-signing abuse are being used to improve delivery and trust. TeamPCP and adjacent Shai-Hulud or Miasma operators continue to target developer ecosystems and cloud credentials. ShinyHunters also remains relevant because recent reporting shows the group still mixes software exploitation, cloud abuse, social engineering, and data-theft extortion.

## Recommended Actions
Prioritize controls that reduce token and session abuse in Microsoft 365 and Entra ID: phishing-resistant MFA for privileged roles, strict conditional access, shorter session lifetime for sensitive apps, and rapid session revocation for exposed users. Expand detections for infostealer fallout, AiTM phishing, mailbox staging into the non-IPM subtree, and anomalous token acquisition from Azure metadata and Graph-related paths. For development and cloud operations, lock internal package scopes to private registries, disable install scripts where practical, and rotate secrets from any developer workstation or CI/CD runner that touched the affected npm ecosystems.

## Sources
- StealC and Amadey: Breaking down infostealers and the cybercrime services that deliver them — https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/
- One intrusion, two cyberattackers: Uncovering parallel threat activity — https://www.microsoft.com/en-us/security/blog/2026/06/22/one-intrusion-two-cyberattackers-uncovering-parallel-threat-activity/
- AI brands as bait: How threat actors are using the AI hype in social engineering — https://www.microsoft.com/en-us/security/blog/2026/06/08/ai-brands-as-bait-how-threat-actors-are-using-the-ai-hype-in-social-engineering/
- New Exchange Online Mailbox Auditing Signal: Visibility into IPM to Non-IPM Copy Activity — https://techcommunity.microsoft.com/t5/microsoft-security-community/new-exchange-online-mailbox-auditing-signal-visibility-into-ipm/ba-p/4526914
- Preinstall to persistence: Inside the Red Hat npm Miasma credential-stealing campaign — https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/
- Malicious npm packages abuse dependency confusion to profile developer environments — https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/
