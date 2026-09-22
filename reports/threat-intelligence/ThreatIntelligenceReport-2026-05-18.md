# Threat Intelligence Report — 2026-05-18

## Executive Summary
Recent reporting continues to show identity-led intrusion paths: adversary-in-the-middle (AiTM) phishing, token/session abuse, and OAuth consent/app abuse that bypasses password resets and weakens MFA as a single control. Microsoft 365-relevant operations also depend heavily on commodity infrastructure that enables high-volume BEC and phishing at scale. The most immediate risk for M365 tenants is AiTM-driven account compromise followed by mailbox rule tampering and downstream BEC activity.

## Key Threats

### Multi-stage AiTM phishing and BEC abusing SharePoint
**Type:** AiTM phishing / BEC
**Severity:** Critical
**MITRE ATT&CK:** T1557 T1566 T1114.003 T1078.004
**CVEs:** N/A
**Affected:** Microsoft 365 (SharePoint/OneDrive), Exchange Online mailboxes, Entra ID identities
**M365/Azure relevance:** Uses trusted SharePoint sharing flows to capture credentials/session artifacts, then weaponizes compromised mailboxes (rules + internal/external phishing) for BEC.
**Summary:** A multi-stage campaign targeted organizations using SharePoint links that looked like normal document-sharing prompts. After initial compromise, attackers created inbox rules to delete/mark-read inbound mail to reduce victim visibility, then sent further phishing from the compromised identity to contacts and distribution lists, and carried out BEC-style mailbox monitoring and reply/deletion to sustain fraud operations.
**Recommendations:** Revoke user sessions (invalidate cookies/tokens) in addition to password resets; hunt for and remove suspicious inbox/forwarding rules; enforce Conditional Access (device compliance, named locations, risk-based policies) and enable continuous access evaluation.
**Source:** Resurgence of a multi‑stage AiTM phishing and BEC campaign abusing SharePoint — https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/

### Criminal virtual desktop infrastructure enabling BEC and mass phishing (RedVDS)
**Type:** Cybercriminal infrastructure / BEC enablement
**Severity:** High
**MITRE ATT&CK:** T1566 T1078.004
**CVEs:** N/A
**Affected:** Exchange Online mailboxes, M365 identity and email security controls
**M365/Azure relevance:** Provides Windows RDP hosts used for phishing, account takeover, and BEC workflows that frequently target Microsoft 365 mailboxes and identities.
**Summary:** Microsoft observed broad cybercriminal use of RedVDS “cheap Windows RDP” instances to run phishing, account takeover, and BEC at scale. Activity attributed to the operator (Storm-2470) was associated with multiple downstream actors leveraging consistent host-image fingerprints and infrastructure to support credential theft and fraud operations.
**Recommendations:** Tighten anti-spoofing posture (SPF/DKIM/DMARC enforcement) and validate “From” headers; alert on risky sign-ins and mailbox rule creation; block known infrastructure indicators where feasible and prioritize investigation of suspicious RDP-backed sender infrastructure.
**Source:** Inside RedVDS: How a single virtual desktop provider fueled worldwide cybercriminal operations — https://www.microsoft.com/en-us/security/blog/2026/01/14/inside-redvds-how-a-single-virtual-desktop-provider-fueled-worldwide-cybercriminal-operations/

### Silk Typhoon abusing stolen keys/credentials and third-party services to reach cloud customers
**Type:** Espionage / supply chain and credential abuse
**Severity:** High
**MITRE ATT&CK:** T1195 T1078.004 T1552
**CVEs:** (varies by victim environment)
**Affected:** IT providers (RMM/PAM/cloud app providers) and downstream customers, including M365/Azure workloads
**M365/Azure relevance:** Post-compromise activity includes abusing deployed Microsoft services; key/credential theft increases risk of Entra ID, Azure, and M365 tenant access.
**Summary:** Microsoft reported a shift in Silk Typhoon tradecraft toward compromising common IT solutions and abusing stolen API keys/credentials from providers (PAM, cloud app, cloud data management) to access downstream customer environments. Once inside, the actor performs recon, collection, and persistence actions consistent with well-resourced espionage operations.
**Recommendations:** Reduce credential exposure (secret scanning, rotate exposed keys, enforce least privilege for API keys/service principals); require phishing-resistant MFA and Conditional Access for admin planes; ensure rapid patching of internet-facing services and monitor for anomalous access to Azure Key Vault and OAuth app credential changes.
**Source:** Silk Typhoon targeting IT supply chain — https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/

### OAuth consent/app abuse for persistent access to Microsoft 365 data
**Type:** OAuth app abuse / token-based persistence
**Severity:** High
**MITRE ATT&CK:** T1528 T1098.001
**CVEs:** N/A
**Affected:** Entra ID enterprise apps, Microsoft Graph permissions, Exchange/SharePoint/OneDrive data
**M365/Azure relevance:** Delegated/app permissions can grant durable access to mail and files without reusing user passwords; remediation requires revoking grants/tokens and removing app credentials.
**Summary:** OAuth “consent phishing” remains a practical path to persistent access: users are tricked into granting a malicious app high-privilege permissions (mail, files, directory). Attackers can blend into legitimate app traffic, exfiltrate data via Microsoft Graph, and extend persistence by adding secrets/certificates to service principals.
**Recommendations:** Restrict user consent and require admin approval for high-risk permissions; monitor for new consent grants and privileged permission changes; inventory and review enterprise apps regularly, and revoke consent/credentials for suspicious apps.
**Source:** Investigating OAuth App Abuse with the Graph Activity Log — https://practical365.com/investigating-oauth-app-abuse-with-the-graph-activity-log/

### PipeMagic modular backdoor used to deploy ransomware after exploiting CVE-2025-29824
**Type:** Malware / ransomware enablement
**Severity:** High
**MITRE ATT&CK:** T1068
**CVEs:** CVE-2025-29824
**Affected:** Windows endpoints; downstream access paths into identity and cloud via stolen credentials/tokens
**M365/Azure relevance:** Ransomware operators frequently pivot from endpoints to identity (Entra ID) and SaaS administration using harvested credentials; early-stage backdoors increase the chance of tenant compromise and data theft.
**Summary:** Microsoft detailed PipeMagic, a modular backdoor attributed to Storm-2460 and observed in attack chains that exploit a Windows CLFS elevation-of-privilege vulnerability (CVE-2025-29824) prior to ransomware deployment. The tooling is designed for flexible module delivery, encrypted communication, and in-memory execution that complicates detection.
**Recommendations:** Patch Windows systems to address CVE-2025-29824 and prioritize exposed/privileged endpoints; enable Defender detections for PipeMagic and investigate certutil/MSBuild abuse chains; harden endpoints used for M365 administration (PAWs, device compliance, and restrictive Conditional Access).
**Source:** Dissecting PipeMagic: Inside the architecture of a modular backdoor framework — https://www.microsoft.com/en-us/security/blog/2025/08/18/dissecting-pipemagic-inside-the-architecture-of-a-modular-backdoor-framework/

### ISP-level AiTM enabling credential/token interception (Secret Blizzard)
**Type:** AiTM / credential and token interception
**Severity:** High
**MITRE ATT&CK:** T1557
**CVEs:** N/A
**Affected:** Users on untrusted networks; Windows connectivity checks and TLS trust chain
**M365/Azure relevance:** Token and credential capture can translate into Entra ID session compromise, especially for users operating on hostile networks where traffic interception is feasible.
**Summary:** Microsoft reported an AiTM campaign by Secret Blizzard targeting diplomatic entities via an ISP/telco position, using captive portal redirection and malware that installs a trusted root certificate to enable TLS interception. The tradecraft is a reminder that session/token theft and interception can undermine controls that rely on normal browser trust decisions.
**Recommendations:** Require trusted network paths for sensitive users (always-on VPN/secure tunnels) and avoid relying on local ISPs in hostile environments; watch for abnormal certificate store changes and unexpected root CA installs; enforce device compliance and Conditional Access that limits token replay usefulness.
**Source:** Frozen in transit: Secret Blizzard’s AiTM campaign against diplomats — https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/

### Infostealer resurgence and ClickFix-style lures driving credential theft (Lumma)
**Type:** Credential theft / infostealer
**Severity:** Medium
**MITRE ATT&CK:** T1566 T1059
**CVEs:** N/A
**Affected:** Windows endpoints; browser-stored credentials and cloud keys
**M365/Azure relevance:** Stolen browser credentials, cookies, and “cloud keys” frequently become the bridge into M365/Entra ID sessions and BEC workflows.
**Summary:** Lumma Stealer activity rebounded after prior disruption, using ClickFix social engineering (fake CAPTCHA-style instructions that lead users to paste commands into a terminal) and in-memory loaders to deploy credential-stealing payloads at scale. The stolen data set commonly includes browser credentials/cookies and other secrets that can be leveraged for account takeover.
**Recommendations:** Block and alert on suspicious “copy/paste into terminal” user workflows where possible (ASR rules, script controls); harden browser credential storage and enforce phishing-resistant authentication; monitor for anomalous sign-ins and token use that indicates cookie/session theft.
**Source:** Once-hobbled Lumma Stealer is back with lures that are hard to resist — https://arstechnica.com/security/2026/02/once-hobbled-lumma-stealer-is-back-with-lures-that-are-hard-to-resist/

## Threat Actor Activity
- **Silk Typhoon**: Espionage activity emphasizing third-party IT compromise and credential/key abuse to reach downstream cloud customers.
- **Secret Blizzard**: AiTM operations from an ISP/telco position enabling token/credential interception via trust/certificate manipulation.
- **Star Blizzard**: Continued spear-phishing adaptation, shifting lures toward WhatsApp account compromise.
- **Storm-2470**: Operator enabling RedVDS infrastructure used by multiple criminal actors for BEC and phishing.
- **Storm-2460**: Financially motivated activity leveraging PipeMagic in ransomware-oriented attack chains.

## Recommended Actions
1. **Assume token theft is in play for phishing incidents**: reset passwords *and* revoke sessions, remove malicious inbox/forwarding rules, and validate device compliance before restoring access.
2. **Lock down OAuth and enterprise app risk**: restrict user consent, review high-privilege permissions, and alert on new app credentials (secrets/certs) added to service principals.
3. **Harden admin and high-value identities**: phishing-resistant MFA for admins, Conditional Access with risk/device signals, and privileged access workstations for M365/Azure administration.
4. **Reduce BEC blast radius**: enforce DMARC (reject/quarantine), enable anti-spoofing controls, and monitor for anomalous outbound email and inbox rule manipulation.
5. **Patch and detect pre-ransomware tooling**: prioritize OS/browser updates, remediate exposed services, and investigate Defender alerts tied to loader/backdoor patterns.

## Sources
- Once-hobbled Lumma Stealer is back with lures that are hard to resist — https://arstechnica.com/security/2026/02/once-hobbled-lumma-stealer-is-back-with-lures-that-are-hard-to-resist/
- Resurgence of a multi‑stage AiTM phishing and BEC campaign abusing SharePoint — https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/
- Inside RedVDS: How a single virtual desktop provider fueled worldwide cybercriminal operations — https://www.microsoft.com/en-us/security/blog/2026/01/14/inside-redvds-how-a-single-virtual-desktop-provider-fueled-worldwide-cybercriminal-operations/
- Silk Typhoon targeting IT supply chain — https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/
- Investigating OAuth App Abuse with the Graph Activity Log — https://practical365.com/investigating-oauth-app-abuse-with-the-graph-activity-log/
- Dissecting PipeMagic: Inside the architecture of a modular backdoor framework — https://www.microsoft.com/en-us/security/blog/2025/08/18/dissecting-pipemagic-inside-the-architecture-of-a-modular-backdoor-framework/
- Frozen in transit: Secret Blizzard’s AiTM campaign against diplomats — https://www.microsoft.com/en-us/security/blog/2025/07/31/frozen-in-transit-secret-blizzards-aitm-campaign-against-diplomats/
