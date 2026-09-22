# Threat Intelligence Report — 2026-08-03

## Executive Summary
Identity-centric intrusion paths remain the main risk to Microsoft 365 and Entra ID environments. The strongest themes in the latest material are Teams and email social engineering, token and OAuth abuse, and infostealer activity that turns browser sessions, SSO tokens, and synced cloud data into follow-on access.

The most urgent threat is the continued use of phishing, vishing, AiTM, and ClickFix tradecraft to capture tokens and valid sessions that bypass normal sign-in controls. The full `later` + `feed` pool was stale overall: the combined pool totaled 350 tagged documents, but `feed` was dominated by January 2026 and older material, so this report relies almost entirely on `later`, which indicates a collection and tagging problem that should be corrected.

## Key Threats

### Teams, email, and AiTM phishing shifting after Tycoon2FA disruption
**Type:** Phishing, BEC, AiTM, social engineering
**Severity:** Critical
**MITRE ATT&CK:** T1566, T1557, T1078
**CVEs:** None
**Affected:** Exchange Online, Microsoft Teams, Entra ID, Microsoft 365 users
**M365/Azure relevance:** Attackers are pivoting into Teams, OAuth redirects, calendar lures, and large-scale BEC workflows that directly target Microsoft 365 identities and collaboration channels.
**Summary:** Microsoft reported that Tycoon2FA-linked phishing volume fell sharply in Q2 2026, but threat actors compensated by scaling Teams-based vishing, QR code phishing, CAPTCHA-gated lures, and automated BEC. One campaign hit more than 67,000 users across 42,000 organizations in under three hours, while another used nested EML files, calendar invites, and a `login.microsoftonline.com` redirect to deliver malware.
**Recommendations:** Enforce phishing-resistant MFA for privileged users; tighten Defender for Office 365 Safe Links, Safe Attachments, and ZAP; review external Teams communication settings and train users to distrust support-themed chats and call prompts.
**Source:** [Email threat landscape: Q2 2026 trends and insights](https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/)

### ClickFix-driven ACR Stealer theft of tokens and Microsoft 365 data
**Type:** Infostealer, ClickFix, credential and token theft
**Severity:** High
**MITRE ATT&CK:** T1204, T1218.011, T1059, T1053.005, T1555.003, T1005
**CVEs:** None
**Affected:** Windows endpoints, Edge and Chromium browsers, OneDrive and SharePoint-synced data
**M365/Azure relevance:** The malware explicitly targets browser credentials, authentication tokens, and enterprise documents stored in Microsoft 365-connected directories.
**Summary:** Microsoft observed two ACR Stealer intrusion chains that begin with ClickFix lures and diverge into WebDAV-delivered loaders or MSHTA plus steganography-assisted in-memory execution. The campaigns stole browser credentials and tokens, accessed Microsoft 365 documents in OneDrive and SharePoint, and used scheduled tasks, obfuscated PowerShell, and in-memory execution to persist.
**Recommendations:** Block `mshta.exe`, risky `rundll32.exe`, and paste-and-run execution paths with ASR and application control; revoke browser-backed cloud sessions after suspected compromise; hunt for suspicious WebDAV, DPAPI, and browser database access.
**Source:** [ACR Stealer: Two observed intrusion chains amid increased threat activity](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/)

### OAuth trust abuse and connected app persistence
**Type:** OAuth abuse, vishing, SaaS identity compromise
**Severity:** High
**MITRE ATT&CK:** T1566.004, T1528, T1671, T1213.004, T1567
**CVEs:** None
**Affected:** OAuth-connected SaaS apps, connected identities, guest access paths
**M365/Azure relevance:** The tradecraft maps directly to Entra-connected app governance, non-human identity risk, consent hygiene, and guest access review, even when the observed target platform is outside Microsoft 365.
**Summary:** Microsoft tied ShinyHunters-style activity to voice phishing, supply-chain compromise, and guest access abuse against SaaS platforms. The core pattern is the abuse of trusted OAuth relationships to inherit user or app privileges, persist without obvious sign-in anomalies, and exfiltrate high-value business data through sanctioned APIs.
**Recommendations:** Audit connected apps and OAuth grants, especially high-privilege and unused ones; review external and guest access paths; add SaaS activity telemetry to identity investigations and treat app consent changes as incident triggers.
**Source:** [Defending SaaS-based applications against ShinyHunters OAuth abuse](https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/)

### Infostealer pipelines converting unmanaged-device theft into M365 access
**Type:** Infostealer-as-a-service, malware delivery, session theft
**Severity:** High
**MITRE ATT&CK:** T1555.003, T1539, T1105, T1053.005, T1078
**CVEs:** None
**Affected:** Personal devices, browsers, VPN credentials, SSO tokens, cloud sessions
**M365/Azure relevance:** Stolen cookies, SSO tokens, and saved credentials can provide downstream access to Entra-backed sessions and Microsoft 365 workloads without tripping normal MFA expectations.
**Summary:** Microsoft’s StealC and Amadey analysis shows how commodity infostealers harvest passwords, cookies, tokens, and local files on unmanaged devices, then feed an access-broker ecosystem that resells enterprise footholds. Microsoft explicitly called out the enterprise risk of a home-device infection yielding corporate VPN credentials, SSO tokens, and session cookies.
**Recommendations:** Reduce browser-stored credential use, require conditional access with token protection where possible, and prioritize detections for abnormal session reuse from non-managed contexts; treat infostealer exposure on personal devices as a cloud-identity incident, not just endpoint hygiene.
**Source:** [StealC and Amadey: Breaking down infostealers and the cybercrime services that deliver them](https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/)

### SharePoint-to-identity compromise in a parallel-actor intrusion
**Type:** Initial access, persistence, hybrid intrusion, ransomware precursor
**Severity:** High
**MITRE ATT&CK:** T1190, T1133, T1098, T1574.002
**CVEs:** Not specified in the source
**Affected:** On-premises SharePoint, hybrid identity, remote admin channels, Windows estates
**M365/Azure relevance:** The case shows how SharePoint exposure can become identity abuse, remote persistence, and ransomware staging across hybrid Microsoft environments.
**Summary:** Microsoft DART described an intrusion where Storm-2603 activity on on-premises SharePoint overlapped with a second unrelated actor, creating a blended incident that obscured attribution and delayed detection. The attackers used Velociraptor, Cloudflare tunnels, Zoho Assist, SSH over Visual Studio Code, and new admin accounts to persist and move through the environment.
**Recommendations:** Prioritize SharePoint and other internet-facing Microsoft server patching; monitor creation of new local and domain admin accounts and remote tunnel tooling; correlate endpoint, identity, and cloud telemetry so blended actor activity is not treated as a single linear intrusion.
**Source:** [One intrusion, two cyberattackers: Uncovering parallel threat activity](https://www.microsoft.com/en-us/security/blog/2026/06/22/one-intrusion-two-cyberattackers-uncovering-parallel-threat-activity/)

### Destructive backdoor activity in Windows environments
**Type:** Wiper, fake ransomware, destructive backdoor
**Severity:** High
**MITRE ATT&CK:** T1485, T1486, T1053.005, T1562
**CVEs:** None
**Affected:** Windows endpoints, scheduled task persistence, hybrid enterprise environments
**M365/Azure relevance:** This is less Microsoft 365-specific than the identity threats above, but it is relevant to cloud-connected Windows estates where a compromise can turn from persistence into destructive impact quickly.
**Summary:** GigaWiper combines multiple destructive capabilities inside one backdoor, including full-disk wiping, fake ransomware encryption with no recovery path, service and registry manipulation, and event log clearing. The blend of persistence, remote control, and destructive commands makes it a serious follow-on risk where identity or endpoint compromise is already present.
**Recommendations:** Keep EDR in block mode and tamper protection enabled, restrict scheduled task abuse, and isolate any host showing both persistence tooling and destructive command preparation; validate backup recoverability for Windows-connected business systems.
**Source:** [GigaWiper: Anatomy of a destructive backdoor assembled from multiple malware](https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/)

## Threat Actor Activity
ShinyHunters-linked operators continued to abuse OAuth trust relationships, vishing, and third-party integrations to persist in SaaS environments. Storm-2603 appeared in a hybrid SharePoint intrusion that overlapped with a second actor, reinforcing that multiple adversaries can operate in the same estate at once. The Tycoon2FA ecosystem remains weakened, but the broader phishing market has adapted by shifting toward Teams vishing, automated BEC, and Microsoft-themed redirect chains rather than abandoning token theft.

## Recommended Actions
Prioritize phishing-resistant MFA for privileged and high-risk users, and review where token protection and Conditional Access can actually prevent session replay instead of only protecting the initial sign-in. Tighten controls on Teams external communications, OAuth app consent, guest access, and unmanaged-device access to Microsoft 365.

Hunt for signs of session and token theft rather than waiting for password resets to surface compromise. Focus on abnormal browser credential access, new connected apps, remote admin tooling, SharePoint exposure, suspicious mailbox access patterns, and endpoint evidence of ClickFix, MSHTA, or WebDAV execution.

Fix the collection itself. The `threat intelligence` tag pool is stale, especially in `feed`, and should be pruned or retagged so recurring reports do not depend on old material when current Microsoft 365 and identity threats are available elsewhere in Reader.

## Sources
- [Email threat landscape: Q2 2026 trends and insights](https://www.microsoft.com/en-us/security/blog/2026/07/23/email-threat-landscape-q2-2026-trends-and-insights/)
- [ACR Stealer: Two observed intrusion chains amid increased threat activity](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/)
- [Defending SaaS-based applications against ShinyHunters OAuth abuse](https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/)
- [GigaWiper: Anatomy of a destructive backdoor assembled from multiple malware](https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/)
- [StealC and Amadey: Breaking down infostealers and the cybercrime services that deliver them](https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/)
- [One intrusion, two cyberattackers: Uncovering parallel threat activity](https://www.microsoft.com/en-us/security/blog/2026/06/22/one-intrusion-two-cyberattackers-uncovering-parallel-threat-activity/)
