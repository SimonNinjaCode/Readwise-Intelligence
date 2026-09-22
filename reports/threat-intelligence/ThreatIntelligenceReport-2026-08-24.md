# Threat Intelligence Report — 2026-08-24

## Executive Summary
The strongest current risks to Microsoft environments are token-centric identity attacks: device code phishing against Entra ID, AiTM phishing against Microsoft 365, and OAuth abuse that turns trusted SaaS integrations into persistence and data-exfiltration channels. Exchange exploitation also remains active, with a half-click Outlook Web Access attack enabling persistent mailbox compromise even after credential resets and workstation rebuilds. The `threat intelligence` tag in Readwise is stale: the combined `later` + `feed` pool is dominated by old or off-scope material, so this report uses the latest 20 fetched documents and narrows them to the current items that materially affect M365, Entra ID, Azure-connected identities, or cloud-linked ransomware exposure.

## Key Threats

### CaptiveCrunch device code and AiTM campaign
**Type:** Device code phishing, AiTM, malware delivery  
**Severity:** Critical  
**MITRE ATT&CK:** T1557, T1528, T1566.004  
**CVEs:** None cited  
**Affected:** Microsoft Entra ID, Microsoft 365, Windows endpoints, corporate travelers using captive portals  
**M365/Azure relevance:** Storm-2945 used captive-portal traffic manipulation to push users into Entra device code and OAuth code phishing, leading to Entra device registration and Microsoft 365 data collection.  
**Summary:** Microsoft tied Storm-2945, a Midnight Blizzard sub-cluster, to hospitality-network traffic manipulation that redirected victims to Microsoft-themed phishing infrastructure and malware. The campaign combines DNS and HTTP manipulation, device code abuse, token theft, and follow-on malware to compromise M365 accounts during travel.  
**Recommendations:** Block device code flow where not required; enforce phishing-resistant MFA and sign-in risk policies; treat hotel and conference Wi-Fi as untrusted and prefer managed hotspots or private connectivity.  
**Source:** [CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/)

### OWAReaper via Exchange OWA XSS
**Type:** Exchange exploitation, persistent mailbox compromise  
**Severity:** Critical  
**MITRE ATT&CK:** T1190, T1056, T1528  
**CVEs:** CVE-2026-42897  
**Affected:** Microsoft Exchange Server, Outlook Web Access accounts, OWA sessions  
**M365/Azure relevance:** The attack targets Microsoft messaging infrastructure directly and can steal OAuth tokens and maintain mailbox access after password resets, creating lasting cloud and email exposure.  
**Summary:** Proofpoint attributed active exploitation of a maximum-severity Exchange OWA XSS bug to TA488. The resulting OWAReaper implant runs in the OWA reading pane, steals saved credentials and OAuth tokens, and persists in server-side settings so reimaging the user device does not evict the attacker.  
**Recommendations:** Patch Exchange immediately; audit and revoke Exchange Web Services and OAuth tokens; clear OWA local storage artifacts and investigate connections to reported C2 domains.  
**Source:** [Max-severity Exchange server flaw under active exploitation by Kremlin hackers](https://arstechnica.com/security/2026/07/kremlin-hackers-are-exploiting-exchange-flaw-to-backdoor-unpatched-networks/)

### Q2 2026 phishing, BEC, and Teams abuse
**Type:** Phishing, BEC, Teams vishing, AiTM  
**Severity:** High  
**MITRE ATT&CK:** T1566.001, T1566.002, T1566.004, T1557  
**CVEs:** None  
**Affected:** Microsoft 365 mailboxes, Microsoft Teams users, Entra-backed sign-ins  
**M365/Azure relevance:** The observed campaigns targeted M365 users at scale, used Microsoft authentication redirects, abused Teams as a social-engineering channel, and continued to pressure token-based identity controls.  
**Summary:** Microsoft saw 7.6 billion phishing emails in Q2 2026, continued BEC automation at scale, and a sharp rise in Teams-based vishing. Tycoon2FA volumes dropped after disruption, but attackers shifted toward other delivery paths, including Microsoft-authentication-linked malware delivery and social engineering through Teams.  
**Recommendations:** Tighten Defender for Office 365 Safe Links/Safe Attachments and ZAP; expand Teams phishing awareness and simulation; enforce passwordless or phishing-resistant MFA for privileged and high-risk users.  
**Source:** [Email threat landscape: Q2 2026 trends and insights](https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/)

### ACR Stealer ClickFix campaigns
**Type:** Infostealer, ClickFix, token theft  
**Severity:** High  
**MITRE ATT&CK:** T1204, T1059.001, T1218.011, T1218.005, T1555  
**CVEs:** None cited  
**Affected:** Windows endpoints, browser credential stores, Microsoft 365 and OneDrive/SharePoint-synced data  
**M365/Azure relevance:** The campaigns explicitly targeted browser credentials, authentication tokens, and Microsoft 365 documents, creating direct risk to cloud access and synchronized enterprise content.  
**Summary:** Microsoft observed two prominent ACR Stealer intrusion chains using ClickFix, WebDAV, Rundll32, MSHTA, obfuscated PowerShell, and in-memory execution. Post-compromise behavior included browser credential theft, token theft, and collection of M365 documents and files from enterprise-synced directories.  
**Recommendations:** Block or constrain MSHTA, Rundll32, and untrusted PowerShell paths; monitor DPAPI activity and browser database access; isolate affected devices and revoke tokens from a clean host.  
**Source:** [ACR Stealer: Two observed intrusion chains amid increased threat activity](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/)

### ShinyHunters-style OAuth abuse against SaaS apps
**Type:** OAuth abuse, SaaS persistence, data exfiltration  
**Severity:** High  
**MITRE ATT&CK:** T1566.004, T1528, T1213.004, T1567  
**CVEs:** None  
**Affected:** Salesforce-connected apps, third-party integrations, non-human identities, downstream SaaS trust relationships  
**M365/Azure relevance:** The core pattern is identity abuse through trusted OAuth relationships, the same trust boundary M365 and Entra administrators need to defend across connected applications and delegated access.  
**Summary:** Microsoft linked multiple campaigns associated with ShinyHunters tradecraft to vishing-led OAuth consent abuse, compromised SaaS integrations, and guest-access misuse. The result was persistent API access and large-scale data exfiltration through sanctioned application access rather than classic credential replay.  
**Recommendations:** Audit connected OAuth apps and guest access; prioritize high-risk non-human identities and third-party integrations; extend monitoring for anomalous API-heavy access and consent activity.  
**Source:** [Defending SaaS-based applications against ShinyHunters OAuth abuse](https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/)

### DeadLock ransomware in hybrid and cloud-connected estates
**Type:** Ransomware, double extortion  
**Severity:** High  
**MITRE ATT&CK:** T1486, T1490, T1562.001  
**CVEs:** None cited  
**Affected:** Windows servers and endpoints, Active Directory services, backup services, OneDrive and other sync clients  
**M365/Azure relevance:** DeadLock explicitly targets backup, sync, and AD-related processes, which raises impact in hybrid estates where identity, file sync, and recovery workflows bridge on-prem and Microsoft cloud services.  
**Summary:** Microsoft described DeadLock as an emerging ransomware operation using decentralized infrastructure for negotiations and leak operations. The malware disables services including Windows Defender, backup tooling, Hyper-V components, AD services, and cloud-sync processes such as OneDrive before encrypting and extorting victims.  
**Recommendations:** Run Defender EDR in block mode and automatic attack disruption; harden backup and sync paths, including Controlled Folder Access where feasible; monitor for service stoppage against AD, backup, and sync components.  
**Source:** [DeadLock ransomware: Breaking down a Rust-based encryptor with decentralized recovery infrastructure](https://www.microsoft.com/en-us/security/blog/2026/08/10/deadlock-ransomware-breaking-down-a-rust-based-encryptor-with-decentralized-recovery-infrastructure/)

## Threat Actor Activity
Midnight Blizzard remained the clearest named actor in-scope through Storm-2945’s CaptiveCrunch operations against travelers and Entra device code flows. TA488, also tracked as Laundry Bear and Void Blizzard, was linked to active exploitation of Exchange OWA for persistent mailbox compromise. Microsoft also tied OAuth-centric SaaS abuse to tradecraft associated with ShinyHunters, while the broader phishing ecosystem continued to show residual Tycoon2FA impact, rising Teams vishing, and automated BEC at scale.

## Recommended Actions
1. Disable or tightly scope device code flow in Entra ID and require phishing-resistant MFA for privileged, traveler, and high-risk users.
2. Patch Exchange immediately, then revoke and review mailbox-related OAuth and Exchange Web Services tokens where OWA exposure exists.
3. Expand detection for token theft patterns: anomalous device registration, suspicious OAuth consent, unusual browser credential access, and Teams-based social engineering.
4. Review OAuth-connected applications, guest access, and non-human identities across Microsoft and third-party SaaS integrations.
5. Harden endpoint execution paths commonly used by ClickFix and stealers, including `mshta.exe`, `rundll32.exe`, remote WebDAV execution, and uncontrolled PowerShell.
6. Treat the Readwise `threat intelligence` tag as a maintenance issue: remove stale and off-scope items so future reports are not diluted by 2023-2025 material.

## Sources
- [CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/)
- [Max-severity Exchange server flaw under active exploitation by Kremlin hackers](https://arstechnica.com/security/2026/07/kremlin-hackers-are-exploiting-exchange-flaw-to-backdoor-unpatched-networks/)
- [Email threat landscape: Q2 2026 trends and insights](https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/)
- [ACR Stealer: Two observed intrusion chains amid increased threat activity](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/)
- [Defending SaaS-based applications against ShinyHunters OAuth abuse](https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/)
- [DeadLock ransomware: Breaking down a Rust-based encryptor with decentralized recovery infrastructure](https://www.microsoft.com/en-us/security/blog/2026/08/10/deadlock-ransomware-breaking-down-a-rust-based-encryptor-with-decentralized-recovery-infrastructure/)
