# Threat Intelligence Report — 2026-08-31

## Executive Summary
ClickFix-style initial access, token theft, and abuse of trusted Microsoft identity flows remain the strongest themes in the latest tagged material. The highest-priority issue for Microsoft 365 and Entra teams is CaptiveCrunch, where Midnight Blizzard infrastructure redirected travelers into AiTM and device code phishing paths tied to Microsoft 365 data theft. The combined `later` + `feed` pool for the `threat intelligence` tag is also stale and noisy: many tagged items are old, off-scope, or product-update material, which is a collection/tagging problem rather than a sign of a quiet threat week.

## Key Threats

### CaptiveCrunch targeting Entra ID and Microsoft 365 travelers
**Type:** AiTM phishing, device code phishing, credential and token theft
**Severity:** Critical
**MITRE ATT&CK:** T1557, T1528, T1566
**CVEs:** None cited
**Affected:** Microsoft Entra ID, Microsoft 365, Windows endpoints on captive-portal networks
**M365/Azure relevance:** The campaign abuses Microsoft identity flows, registers Entra devices, steals Microsoft 365 data, and uses lookalike domains for Microsoft services.
**Summary:** Microsoft tied Storm-2945, a Midnight Blizzard sub-cluster, to captive-portal traffic manipulation that redirected travelers into AiTM infrastructure and device code/OAuth phishing. The follow-on malware steals browser credentials, Microsoft 365 SSO tokens, Azure AD tokens, and Token Broker artifacts, giving the actor durable cloud access beyond the initial phish.
**Recommendations:** Block device code flow where it is not required. Tighten Conditional Access around risky sign-ins and phishing-resistant MFA. Treat hotel and conference Wi-Fi as hostile and monitor for sign-ins tied to the published campaign domains and IPs.
**Source:** CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft — https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/

### TerminalFix reverse-tunnel intrusion chain
**Type:** ClickFix, DLL sideloading, reverse tunneling, pre-ransomware intrusion
**Severity:** High
**MITRE ATT&CK:** T1189, T1059.001, T1574.002, T1547.001, T1053.005, T1572
**CVEs:** None cited
**Affected:** Windows endpoints, Active Directory environments, internal enterprise networks
**M365/Azure relevance:** The malware performs AD discovery, targets mail and server infrastructure, and Microsoft explicitly recommends tightening Defender for Office 365 and Defender XDR coverage.
**Summary:** TerminalFix moved the ClickFix pattern from Win+R into Windows Terminal and PowerShell, then used DLL sideloading, steganographic payload retrieval, scheduled-task persistence, and a Python reverse WebSocket tunnel. The critical point is the pivot capability: once a user runs the pasted command, the host becomes a network proxy for further credential theft, lateral movement, and potential ransomware deployment.
**Recommendations:** Train users to treat CAPTCHA pages that ask for pasted commands as malicious. Hunt for `LockScreenContentServer.exe` outside standard paths and for `pythonw.exe` tunneling activity. Prioritize containment and credential rotation on any domain-joined host that matches the chain.
**Source:** TerminalFix campaign deploys a reverse tunnel through multistage intrusion — https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/

### AI control-plane compromise hitting Azure-connected workloads
**Type:** Exploitation of exposed AI infrastructure, credential theft, cryptomining
**Severity:** High
**MITRE ATT&CK:** T1190, T1552.001, T1059, T1496, T1098.004, T1053.003
**CVEs:** CVE-2026-42271, CVE-2026-48710, CVE-2026-49869
**Affected:** LiteLLM, RAGFlow, Kestra, Azure Database for PostgreSQL, AI gateway runtimes
**M365/Azure relevance:** One observed path accessed Azure Database for PostgreSQL and harvested secrets that can expose downstream AI, SaaS, and tenant-integrated workflows.
**Summary:** Microsoft documented multiple intrusions against AI control points, with the clearest Azure-relevant case involving LiteLLM. Attackers harvested model-provider keys and database strings, accessed Azure PostgreSQL-backed LiteLLM data, established persistence, and monetized compromised compute through XMRig-style mining.
**Recommendations:** Treat AI gateways as privileged infrastructure. Remove internet exposure from admin and test surfaces, especially MCP-related paths. Monitor AI runtimes for access to `/proc/1/environ`, unusual Python database access, and outbound connections to raw-IP or mining infrastructure.
**Source:** When AI infrastructure becomes the target: Securing gateways and control points — https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/

### ACR Stealer campaigns targeting cloud sessions and enterprise data
**Type:** ClickFix, infostealer, browser token theft
**Severity:** High
**MITRE ATT&CK:** T1204, T1059.001, T1218.005, T1539, T1555
**CVEs:** None cited
**Affected:** Windows endpoints, Chromium browsers, Microsoft 365 documents, OneDrive and SharePoint-synced data
**M365/Azure relevance:** The malware steals browser credentials, session tokens, Microsoft 365 and Azure AD tokens, and explicitly targets OneDrive and SharePoint content for collection.
**Summary:** Defender Experts observed two ACR Stealer chains using ClickFix, WebDAV or MSHTA delivery, PowerShell obfuscation, and staged in-memory loaders. The operational impact for Microsoft tenants is direct session theft and theft of synchronized enterprise files, which can bypass simple password resets if session tokens remain valid.
**Recommendations:** Monitor for ClickFix, WebDAV, MSHTA, and browser debugging abuse. Invalidate sessions, not just passwords, on affected users. Add detections for suspicious access to Token Broker artifacts and browser cookie stores.
**Source:** ACR Stealer: Two observed intrusion chains amid increased threat activity — https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/

### Phishing and BEC pressure on Exchange Online, Teams, and Microsoft auth flows
**Type:** Credential phishing, BEC, Teams social engineering, malware delivery
**Severity:** High
**MITRE ATT&CK:** T1566.001, T1566.002, T1586, T1078
**CVEs:** None cited
**Affected:** Exchange Online, Microsoft Teams, Microsoft Entra ID, Windows endpoints
**M365/Azure relevance:** The quarter’s campaigns abused Microsoft login infrastructure, nested EML and ICS delivery, Teams impersonation, and large-scale BEC against role accounts in Microsoft 365 environments.
**Summary:** Microsoft recorded 7.6 billion email-based phishing threats in Q2 2026. Even after the Tycoon2FA disruption cut linked phishing volume by 92% from pre-disruption levels, teams still faced high-volume QR phishing, CAPTCHA-gated phishing, Teams vishing growth, and campaigns that routed users through `login.microsoftonline.com` before handing them malware.
**Recommendations:** Review Defender for Office 365 recommended settings, Safe Links, Safe Attachments, and ZAP coverage. Expand phishing simulations into Teams. Tighten Conditional Access and phishing-resistant MFA for privileged and frequently targeted users.
**Source:** Email threat landscape: Q2 2026 trends and insights — https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/

### DeadLock ransomware disrupting Windows and AD-heavy environments
**Type:** Ransomware, double extortion
**Severity:** High
**MITRE ATT&CK:** T1486, T1070.001, T1562.001, T1490
**CVEs:** None cited
**Affected:** Windows endpoints, backup services, Hyper-V, Active Directory services, cloud sync applications
**M365/Azure relevance:** DeadLock kills OneDrive and other sync processes, disables recovery-related services, and targets AD-related services, increasing the risk of broad business disruption in hybrid Microsoft estates.
**Summary:** Microsoft described DeadLock as an active ransomware operation using decentralized recovery and leak infrastructure to make disruption harder. Its pre-encryption behavior includes disabling backup and security services, clearing logs, killing remote access and cloud-sync processes, and targeting services tied to AD and virtualization before encryption starts.
**Recommendations:** Prioritize immutable backups, recovery drills, and tamper protection. Watch for service-disable patterns around Defender, VSS, and AD services. Segment admin access and reduce standing privilege on systems that can reach domain or backup infrastructure.
**Source:** DeadLock ransomware: Breaking down a Rust-based encryptor with decentralized recovery infrastructure — https://www.microsoft.com/en-us/security/blog/2026/08/10/deadlock-ransomware-breaking-down-a-rust-based-encryptor-with-decentralized-recovery-infrastructure/

### ChainDrop supply-chain worm stealing cloud and CI/CD secrets
**Type:** Software supply-chain compromise, credential theft
**Severity:** High
**MITRE ATT&CK:** T1195, T1552.001, T1078, T1071.001
**CVEs:** None cited
**Affected:** npm packages, developer workstations, CI/CD pipelines, cloud credentials, Kubernetes and Vault secrets
**M365/Azure relevance:** The worm steals cloud and developer secrets that can expose Azure-integrated build systems, identity material, and downstream SaaS or application environments.
**Summary:** ChainDrop affected more than 400 npm packages and used a Mini Shai-Hulud variant to steal package, GitHub, cloud, Kubernetes, and Vault credentials. The risk is less about the package names themselves and more about what lives in developer and pipeline environments once the worm executes.
**Recommendations:** Rotate secrets on any environment that used affected packages, especially CI/CD credentials. Enforce package allow-listing and preinstall-hook controls where possible. Hunt for unusual package publishing, repo token use, and cloud secret access after package installation events.
**Source:** ChainDrop supply chain compromise: Anatomy of a self-propagating worm — https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/

## Threat Actor Activity
Storm-2945, assessed by Microsoft as a Midnight Blizzard sub-cluster, drove the most relevant Microsoft-focused identity activity through CaptiveCrunch and follow-on device code/OAuth abuse. Financially motivated operators behind ACR Stealer and DeadLock continued to favor user-driven execution, token theft, and post-compromise monetization. Supply-chain activity tied to TeamPCP and the Mini Shai-Hulud/ChainDrop ecosystem remained operationally important because it exposed cloud, package, and pipeline credentials that can be reused against Microsoft-connected enterprise environments.

## Recommended Actions
1. Block Microsoft Entra device code flow except where there is a hard business need, and review Conditional Access coverage for risky sign-ins, token protection, and phishing-resistant MFA.
2. Hunt aggressively for ClickFix and TerminalFix patterns across endpoints, browser downloads, PowerShell, MSHTA, WebDAV, scheduled tasks, and suspicious `pythonw.exe` or reverse-tunnel execution.
3. Invalidate sessions as well as passwords after suspected compromise, especially for browser tokens, Token Broker artifacts, and OAuth-granted application access.
4. Review Defender for Office 365, Teams protections, Safe Links, Safe Attachments, and ZAP to close gaps in email, calendar, and collaboration-borne phishing.
5. Treat AI gateways, orchestration services, and pipeline systems as privileged assets; remove public exposure, rotate secrets, and monitor for secret access or cloud-database misuse.
6. Clean up the Readwise `threat intelligence` tag set so future reports are not diluted by stale, generic, or non-threat entries.

## Sources
- TerminalFix campaign deploys a reverse tunnel through multistage intrusion — https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/
- When AI infrastructure becomes the target: Securing gateways and control points — https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/
- DeadLock ransomware: Breaking down a Rust-based encryptor with decentralized recovery infrastructure — https://www.microsoft.com/en-us/security/blog/2026/08/10/deadlock-ransomware-breaking-down-a-rust-based-encryptor-with-decentralized-recovery-infrastructure/
- CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft — https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/
- Email threat landscape: Q2 2026 trends and insights — https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/
- ACR Stealer: Two observed intrusion chains amid increased threat activity — https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/
- ChainDrop supply chain compromise: Anatomy of a self-propagating worm — https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/
