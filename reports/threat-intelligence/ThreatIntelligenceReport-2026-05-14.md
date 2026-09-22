# Threat Intelligence Report — 2026-05-14

## Executive Summary
This week’s signal is dominated by identity-centric intrusion paths: AiTM token theft, device code abuse at scale, and OAuth redirect manipulation that turns trusted login URLs into delivery infrastructure. The most urgent risk is durable account takeover without passwords (session tokens/device codes), compounded by stealthy third-party access paths that blend into normal admin tooling.

## Key Threats

### Third-party compromise abusing trusted admin tooling (HPE Operations Agent)
**Type:** Third-party compromise / living-off-the-land intrusion  
**Severity:** Critical  
**MITRE ATT&CK:** T1199 T1059.001 T1505.003 T1003  
**CVEs:** N/A  
**Affected:** Enterprise identity infrastructure and internet-facing servers; environments with outsourced IT management relationships  
**M365/Azure relevance:** Credential theft and durable access commonly translate into mailbox access, OAuth app abuse, and downstream Microsoft 365 compromise once identities are harvested.  
**Summary:** Microsoft Incident Response investigated a stealthy intrusion where an attacker operated through a compromised third-party IT provider and a signed enterprise management tool (HPE Operations Agent) to execute scripts/binaries that resembled routine admin activity. The incident included credential-theft steps and web-based persistence, illustrating how “trusted” operational relationships and tooling become the delivery mechanism rather than exploits.  
**Recommendations:** Enforce Conditional Access for admin access (MFA + device compliance) and tightly scope partner access; audit third-party tooling execution paths and script deployment; hunt for suspicious LSA notification packages/network providers and webshell activity on exposed servers.  
**Source:** Undermining the trust boundary: Investigating a stealthy intrusion through third-party compromise — https://www.microsoft.com/en-us/security/blog/2026/05/12/undermining-the-trust-boundary-investigating-a-stealthy-intrusion-through-third-party-compromise/

### “Code of conduct” AiTM phishing driving token compromise
**Type:** AiTM phishing / session token theft  
**Severity:** High  
**MITRE ATT&CK:** T1566.002 T1550.004 T1078  
**CVEs:** N/A  
**Affected:** Microsoft 365 identities; email users in targeted orgs  
**M365/Azure relevance:** AiTM captures tokens/cookies to bypass non-phishing-resistant MFA, enabling immediate access to Outlook/OneDrive/SharePoint and rapid BEC-style follow-on.  
**Summary:** Microsoft observed a multi-stage phishing chain using “code of conduct” lures, CAPTCHA and staging pages, and legitimate email services to distribute messages at scale, culminating in an AiTM proxy flow that captured authentication tokens. The activity targeted tens of thousands of users and relied on urgency/pressure messaging to drive interaction.  
**Recommendations:** Move high-risk users to phishing-resistant MFA (FIDO2/WHfB) and enable token protection where applicable; tighten Defender for Office 365 policies (Safe Links/Safe Attachments, ZAP) and block listed IOCs; monitor risky sign-ins and correlate with URL click telemetry.  
**Source:** Breaking the code: Multi-stage ‘code of conduct’ phishing campaign leads to AiTM token compromise — https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/

### AI-enabled device code phishing (EvilToken) compromising Entra accounts
**Type:** Device code phishing / token-based account takeover  
**Severity:** High  
**MITRE ATT&CK:** T1566.002 T1528 T1114.003  
**CVEs:** N/A  
**Affected:** Microsoft Entra ID (device code flow), Exchange Online, Microsoft Graph  
**M365/Azure relevance:** Device code abuse can grant access without password capture and is effective against many MFA deployments; post-compromise actions included Graph recon and inbox-rule persistence.  
**Summary:** Microsoft reported a scaled device code phishing campaign using automation and dynamic code generation to defeat timing constraints and increase success rates, tied to the EvilToken PhaaS ecosystem. The observed follow-on focused on high-value targets with mailbox rule persistence, email exfiltration, and Graph-based recon to map org structure and permissions.  
**Recommendations:** Restrict device code flow where feasible and monitor device-code sign-ins aggressively; alert on unusual Exchange inbox rule creation and “MailItemsAccessed” anomalies; enforce least-privilege and strengthen CA policies for risky sign-ins and unmanaged devices.  
**Source:** Inside an AI‑enabled device code phishing campaign — https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/

### OAuth redirection abuse for phishing and malware delivery
**Type:** OAuth application abuse / redirect-based delivery  
**Severity:** High  
**MITRE ATT&CK:** T1566.002 T1204.001 T1583.001  
**CVEs:** N/A  
**Affected:** Microsoft Entra ID OAuth apps; users targeted by OAuth redirect URLs  
**M365/Azure relevance:** Redirect chains originating on Entra auth endpoints can bypass basic URL reputation controls, steering users into AiTM frameworks or malware delivery while appearing “legitimate.”  
**Summary:** Microsoft observed attackers abusing OAuth redirection behavior by registering malicious apps with attacker-controlled redirect URIs, then distributing crafted links that route victims from trusted identity provider URLs to malicious infrastructure. Microsoft disabled observed OAuth applications, but the technique persists and benefits from user trust in authentication flows.  
**Recommendations:** Audit and constrain enterprise app consent and publisher verification; detect phishing emails containing OAuth URLs (including `prompt=none`) and suspicious `state` parameter usage; review sign-in telemetry for anomalous OAuth app activity and block known malicious client IDs/IOCs.  
**Source:** OAuth redirection abuse enables phishing and malware delivery — https://www.microsoft.com/en-us/security/blog/2026/03/02/oauth-redirection-abuse-enables-phishing-and-malware-delivery/

### Dirty Frag Linux privilege escalation (active attack)
**Type:** Vulnerability exploitation (post-compromise LPE)  
**Severity:** High  
**MITRE ATT&CK:** T1068  
**CVEs:** CVE-2026-43284 CVE-2026-43500  
**Affected:** Linux (kernel networking/memory-fragment components); enterprise Linux and OpenShift estates  
**M365/Azure relevance:** In cloud and hybrid environments, LPE increases blast radius after initial access (webshell/container escape), enabling credential theft and lateral movement into identity and SaaS administration.  
**Summary:** Microsoft reported active exploitation risk for “Dirty Frag,” a Linux local privilege escalation technique affecting esp4/esp6 and rxrpc paths, designed for more reliable escalation than timing-dependent LPEs. The risk is highest where attackers already gained local execution (SSH, webshells, containers, low-priv service accounts).  
**Recommendations:** Patch kernels per vendor advisories as priority; disable unused rxrpc and evaluate temporarily disabling IPsec/xfrm components where safe; increase monitoring for privilege escalation signals and verify integrity post-mitigation.  
**Source:** Active attack: Dirty Frag Linux vulnerability expands post-compromise risk — https://www.microsoft.com/en-us/security/blog/2026/05/08/active-attack-dirty-frag-linux-vulnerability-expands-post-compromise-risk/

### Tycoon2FA AiTM phishing-as-a-service targeting Microsoft 365
**Type:** PhaaS / AiTM token + cookie interception  
**Severity:** High  
**MITRE ATT&CK:** T1566.002 T1550.004 T1567.002  
**CVEs:** N/A  
**Affected:** Microsoft 365 (Outlook, OneDrive, SharePoint); broad enterprise user base  
**M365/Azure relevance:** Directly impersonates M365 sign-in flows and can retain access after password reset unless sessions/tokens are revoked.  
**Summary:** Microsoft documented Tycoon2FA operations at scale, including infrastructure, operator tooling, and evasion (CAPTCHA, fingerprinting, obfuscation). The service enabled widespread M365 credential + session interception, lowering the barrier for commodity actors to run AiTM campaigns.  
**Recommendations:** Enforce phishing-resistant MFA for high-risk roles and tighten session controls (sign-in frequency, token protection where available); harden email ingress against QR/HTML attachment lures; operationalize rapid session revocation playbooks after suspected AiTM compromise.  
**Source:** Inside Tycoon2FA: How a leading AiTM phishing kit operated at scale — https://www.microsoft.com/en-us/security/blog/2026/03/04/inside-tycoon2fa-how-a-leading-aitm-phishing-kit-operated-at-scale/

### Kazuar modular P2P botnet used by Secret Blizzard
**Type:** Nation-state malware / modular botnet C2  
**Severity:** High  
**MITRE ATT&CK:** T1027 T1497 T1105 T1071 T1041  
**CVEs:** N/A  
**Affected:** Target environments of espionage operations; endpoints in government/diplomatic sectors  
**M365/Azure relevance:** Long-term endpoint access and credential collection commonly precede identity abuse (Entra sign-ins, mailbox access, app registration abuse) and should be treated as a likely precursor to M365 impact.  
**Summary:** Microsoft attributed an evolved, modular Kazuar ecosystem to Secret Blizzard, describing a botnet architecture that reduces observability by routing external communications through a leader node and distributing functionality across Kernel/Bridge/Worker modules. The design supports persistence and covert access suitable for long-duration intelligence collection.  
**Recommendations:** Prioritize endpoint isolation and credential reset workflows for suspected Secret Blizzard intrusion; hunt for behaviors consistent with staged working directories, IPC routing, and unusual leader-node communications patterns; ensure Defender XDR is integrated across endpoint + identity signals for rapid containment.  
**Source:** Kazuar: Anatomy of a nation-state botnet — https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/

## Threat Actor Activity
Secret Blizzard; Storm-1747.

## Recommended Actions
- Require phishing-resistant MFA for admins and high-risk users; tighten session/token controls and enforce rapid token/session revocation on suspected compromise.
- Reduce OAuth abuse paths: restrict user consent, audit enterprise apps, and monitor anomalous OAuth redirects/device-code sign-ins.
- Harden email ingress (Defender for Office 365) for link-based and attachment-based phishing; correlate URL clicks with risky sign-ins and mailbox-rule changes.
- Treat third-party access as a core identity perimeter: enforce least privilege, CA policies, and high-fidelity auditing for MSP/partner tooling.
- Patch and monitor Linux estates used for cloud workloads; prioritize LPE exposure that amplifies post-compromise control.

## Sources
- Kazuar: Anatomy of a nation-state botnet — https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/  
- Undermining the trust boundary: Investigating a stealthy intrusion through third-party compromise — https://www.microsoft.com/en-us/security/blog/2026/05/12/undermining-the-trust-boundary-investigating-a-stealthy-intrusion-through-third-party-compromise/  
- Active attack: Dirty Frag Linux vulnerability expands post-compromise risk — https://www.microsoft.com/en-us/security/blog/2026/05/08/active-attack-dirty-frag-linux-vulnerability-expands-post-compromise-risk/  
- Breaking the code: Multi-stage ‘code of conduct’ phishing campaign leads to AiTM token compromise — https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/  
- Inside an AI‑enabled device code phishing campaign — https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/  
- OAuth redirection abuse enables phishing and malware delivery — https://www.microsoft.com/en-us/security/blog/2026/03/02/oauth-redirection-abuse-enables-phishing-and-malware-delivery/  
- Inside Tycoon2FA: How a leading AiTM phishing kit operated at scale — https://www.microsoft.com/en-us/security/blog/2026/03/04/inside-tycoon2fa-how-a-leading-aitm-phishing-kit-operated-at-scale/  