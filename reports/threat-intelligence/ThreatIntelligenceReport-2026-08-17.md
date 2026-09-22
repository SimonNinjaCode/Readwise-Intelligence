# Threat Intelligence Report — 2026-08-17

## Executive Summary
Current Microsoft 365 and Entra-relevant signal in the latest Reader set centers on active Exchange exploitation, Entra-focused adversary-in-the-middle credential theft, OAuth abuse, ClickFix-delivered token theft, and ransomware or supply-chain activity that can spill into cloud identities and admin workflows. The most urgent item is active exploitation of CVE-2026-42897 against Exchange OWA, because it turns a single opened message into persistent mailbox access.

Current signal came entirely from `later`. The `feed` items tagged `threat intelligence` remained stale and did not contribute any document to the latest 20 unique articles.

## Key Threats

### Exchange OWAReaper Half-Click Exploitation
**Type:** Exchange server exploitation and mailbox compromise
**Severity:** Critical
**MITRE ATT&CK:** T1190, T1059.007, T1505
**CVEs:** CVE-2026-42897
**Affected:** Microsoft Exchange Server, Outlook Web Access
**M365/Azure relevance:** Direct risk to Exchange mailboxes, session trust, and downstream identity data.
**Summary:** TA488, also tracked as Laundry Bear and Void Blizzard, is exploiting a maximum-severity XSS flaw in Exchange OWA to install the OWAReaper browser implant. Opening a malicious email in OWA is enough to trigger compromise, and the resulting access can survive credential rotation and disk reimaging.
**Recommendations:** Patch Exchange for CVE-2026-42897 immediately. Reduce or isolate external OWA exposure where possible. Hunt for anomalous OWA JavaScript, mailbox-access anomalies, and post-compromise credential use.
**Source:** [Max-severity Exchange server flaw under active exploitation by Kremlin hackers](https://arstechnica.com/security/2026/07/kremlin-hackers-are-exploiting-exchange-flaw-to-backdoor-unpatched-networks/)

### Captive Portal AiTM Against Entra and Microsoft 365
**Type:** Credential theft, device-code abuse, and malware delivery
**Severity:** High
**MITRE ATT&CK:** T1557, T1566.002, T1528
**CVEs:** None
**Affected:** Travelers using captive portals, Microsoft Entra accounts, Microsoft 365 data
**M365/Azure relevance:** The campaign explicitly abuses Microsoft Entra device code and OAuth flows and has already led to Microsoft 365 data collection.
**Summary:** Microsoft attributes CaptiveCrunch to Storm-2945, a Midnight Blizzard sub-cluster that manipulates hospitality-network traffic to redirect users through attacker-controlled infrastructure. The campaign combines malware delivery with follow-on AiTM phishing and Entra device-code abuse to collect Microsoft 365 data.
**Recommendations:** Block device code flow unless there is a documented business need. Enforce phishing-resistant MFA, token protection, and Conditional Access controls for unmanaged devices and risky travel. Brief traveling staff to avoid reauthentication prompts from captive portals requesting corporate credentials.
**Source:** [CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/)

### M365 Phishing Shift Toward AiTM, BEC, and Teams Vishing
**Type:** Phishing, BEC, and token theft
**Severity:** High
**MITRE ATT&CK:** T1566.001, T1566.002, T1566.004, T1539
**CVEs:** None
**Affected:** Microsoft 365 email users, Teams users, browser sessions
**M365/Azure relevance:** The campaigns target Microsoft-authenticated workflows, mailbox users, and reusable session material tied to Entra-backed services.
**Summary:** Microsoft’s Q2 2026 telemetry shows Tycoon2FA-linked phishing volume fell after disruption, but attackers compensated with QR phishing, CAPTCHA-gated lures, automated BEC delivery, and strong growth in Teams-based social engineering. Microsoft also highlighted token-compromise chains using trusted redirects, nested mail artifacts, and Microsoft-themed lures.
**Recommendations:** Tighten anti-phishing and safe-link controls for QR and attachment-heavy workflows. Review Teams external-access exposure and voice-phishing escalation paths. Expand detections for suspicious OAuth redirects, abnormal mailbox-sending behavior, and user clicks on newly created credential-harvesting domains.
**Source:** [Email threat landscape: Q2 2026 trends and insights](https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/)

### OAuth Abuse Against Trusted SaaS Relationships
**Type:** OAuth abuse, vishing, and data exfiltration
**Severity:** High
**MITRE ATT&CK:** T1566.004, T1528, T1098.001, T1567
**CVEs:** None
**Affected:** OAuth-connected SaaS applications, guest access paths, third-party integrations
**M365/Azure relevance:** The same consent, token, and cross-tenant trust weaknesses apply to Entra-integrated SaaS applications and app-to-app access paths.
**Summary:** Microsoft linked ShinyHunters-associated activity to campaigns that used vishing, supply-chain compromise, and misconfigured guest access to abuse trusted OAuth relationships. The result was persistent access, inherited privileges, and large-scale data access without relying on a native product vulnerability.
**Recommendations:** Audit Entra enterprise applications and OAuth grants for excessive scopes. Review guest-access paths and cross-tenant trust settings. Require stronger admin-consent governance and monitor for unusual app consent, token issuance, and bulk data access.
**Source:** [Defending SaaS-based applications against ShinyHunters OAuth abuse](https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/)

### ClickFix-Delivered Credential and Token Theft
**Type:** Infostealer delivery and session theft
**Severity:** High
**MITRE ATT&CK:** T1204.002, T1218.011, T1059.001, T1555.003
**CVEs:** None
**Affected:** Windows endpoints, browsers, cached credentials, authentication tokens
**M365/Azure relevance:** Browser credentials and tokens stolen from enterprise endpoints can be replayed into Microsoft 365, Entra ID, and cloud admin workflows.
**Summary:** Microsoft observed ACR Stealer campaigns using ClickFix lures, WebDAV delivery, obfuscated PowerShell, MSHTA, and steganography-assisted execution to steal browser credentials, authentication tokens, and enterprise documents. In parallel, Microsoft documented a macOS ClickFix campaign that now hides infostealer lures behind browser-fingerprinting gates, reducing crawler and sandbox visibility.
**Recommendations:** Block or warn on ClickFix-style user-executed command patterns. Monitor for WebDAV, MSHTA, suspicious terminal usage, and obfuscated PowerShell on user endpoints. Force reauthentication and investigate token reuse after suspected endpoint compromise.
**Source:** [ACR Stealer: Two observed intrusion chains amid increased threat activity](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/); [From open lures to cloaked gates: How a macOS ClickFix campaign learned to hide](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/)

### Ransomware and Supply-Chain Theft With Cloud Spillover
**Type:** Ransomware and software supply-chain compromise
**Severity:** High
**MITRE ATT&CK:** T1195.001, T1486, T1552.001, T1567
**CVEs:** None
**Affected:** Developer workstations, CI/CD runners, cloud credentials, enterprise networks
**M365/Azure relevance:** Compromised engineering environments and stolen secrets can expose Azure credentials, app registrations, Key Vault material, and cloud-connected admin workflows.
**Summary:** Microsoft described DeadLock as an emerging ransomware operation using double extortion and resilient decentralized infrastructure. In parallel, Microsoft detailed ChainDrop and the AsyncAPI compromise, both designed to steal credentials from developers and build systems and to spread through trusted software supply paths.
**Recommendations:** Rotate credentials reachable from affected developer or build environments. Move CI/CD and automation to workload identity where possible. Validate backup and recovery controls for hybrid environments and protect identity infrastructure needed for tenant recovery.
**Source:** [DeadLock ransomware: Breaking down a Rust-based encryptor with decentralized recovery infrastructure](https://www.microsoft.com/en-us/security/blog/2026/08/10/deadlock-ransomware-breaking-down-a-rust-based-encryptor-with-decentralized-recovery-infrastructure/); [ChainDrop supply chain compromise: Anatomy of a self-propagating worm](https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/); [Unpacking the AsyncAPI npm supply chain compromise and import-time payload delivery](https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/)

## Threat Actor Activity
Midnight Blizzard and its Storm-2945 sub-cluster remain active against credential-rich travel workflows and Entra authentication paths. TA488, also tracked as Laundry Bear and Void Blizzard, is tied to active Exchange half-click exploitation. ShinyHunters-associated operators continue to abuse OAuth trust relationships and guest access rather than a direct product flaw. Microsoft also described sustained criminal activity around ACR Stealer delivery chains and DeadLock ransomware affiliates.

## Recommended Actions
1. Patch or isolate internet-facing Exchange immediately, with specific focus on CVE-2026-42897 and OWA exposure.
2. Review Entra Conditional Access for token protection, device trust, risky travel, and device-code restrictions.
3. Audit OAuth grants, admin-consent workflows, guest access, and cross-tenant trust relationships for SaaS applications tied to Microsoft identities.
4. Hunt for ClickFix, WebDAV, MSHTA, suspicious terminal execution, obfuscated PowerShell, and abnormal mailbox or Teams activity.
5. Rotate secrets reachable from developer workstations and CI/CD, especially Azure, GitHub, npm, and vault credentials.
6. Enforce phishing-resistant MFA for privileged users and reduce reliance on reusable browser sessions.
7. Validate recovery readiness for destructive or ransomware incidents by protecting backups, admin endpoints, and identity-control infrastructure.

## Sources
- [Max-severity Exchange server flaw under active exploitation by Kremlin hackers](https://arstechnica.com/security/2026/07/kremlin-hackers-are-exploiting-exchange-flaw-to-backdoor-unpatched-networks/)
- [CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/)
- [Email threat landscape: Q2 2026 trends and insights](https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/)
- [Defending SaaS-based applications against ShinyHunters OAuth abuse](https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/)
- [ACR Stealer: Two observed intrusion chains amid increased threat activity](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/)
- [From open lures to cloaked gates: How a macOS ClickFix campaign learned to hide](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/)
- [DeadLock ransomware: Breaking down a Rust-based encryptor with decentralized recovery infrastructure](https://www.microsoft.com/en-us/security/blog/2026/08/10/deadlock-ransomware-breaking-down-a-rust-based-encryptor-with-decentralized-recovery-infrastructure/)
- [ChainDrop supply chain compromise: Anatomy of a self-propagating worm](https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/)
- [Unpacking the AsyncAPI npm supply chain compromise and import-time payload delivery](https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/)
