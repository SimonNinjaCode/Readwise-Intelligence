# Threat Intelligence Report — 2026-07-20

## Executive Summary
Current Microsoft 365 and Entra-relevant reporting is dominated by token theft, device code phishing, and OAuth abuse rather than software exploitation against Microsoft cloud services themselves. The most urgent risk is large-scale identity compromise through device code phishing and AiTM tradecraft that survives password resets by abusing valid tokens, session cookies, and inbox-rule persistence.

The tagged Readwise collection is stale: after ranking the latest 20 documents from the full `later` + `feed` pool, many recent items were unrelated to Microsoft identity or cloud threats. This report therefore focuses only on the subset of current reporting that is materially relevant to Microsoft 365, Entra ID, BEC, AiTM, and cloud-impacting destructive activity.

## Key Threats

### AI-enabled device code phishing against Microsoft 365
**Type:** Credential theft / token theft / phishing  
**Severity:** Critical  
**MITRE ATT&CK:** T1566, T1528, T1078, T1114  
**CVEs:** None  
**Affected:** Microsoft 365, Microsoft Entra ID, Microsoft Graph, Exchange Online  
**M365/Azure relevance:** Direct abuse of the Microsoft device code flow to obtain valid access and refresh tokens for cloud identities.  
**Summary:** Microsoft reported a large-scale campaign using dynamic device-code generation, Railway-hosted automation, Cloudflare Workers, and role-tailored lures to capture valid tokens at scale. Post-compromise activity included Graph reconnaissance, device registration, inbox-rule creation, and email exfiltration.  
**Recommendations:** Block device code flow except where required; revoke refresh tokens and force reauthentication for suspected victims; monitor Entra sign-ins for device-code patterns and suspicious infrastructure.  
**Source:** [Inside an AI-enabled device code phishing campaign](https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/)

### Railway-hosted token replay infrastructure targeting Microsoft 365
**Type:** Credential theft infrastructure / token replay  
**Severity:** Critical  
**MITRE ATT&CK:** T1528, T1078, T1583, T1584  
**CVEs:** None  
**Affected:** Microsoft 365 identities, Entra ID, Exchange Online, SharePoint Online  
**M365/Azure relevance:** Huntress observed Railway being used as clean cloud infrastructure for Microsoft 365 device-code phishing and token replay.  
**Summary:** Huntress documented a campaign affecting more than 340 organizations, with attackers using Railway IP space, Cloudflare Workers, Vercel, AWS, and compromised websites to generate live device codes and replay tokens. The campaign used highly varied lures, including SharePoint, DocuSign, voicemail, and Microsoft Forms themes, and targeted finance, legal, nonprofit, real estate, manufacturing, and government organizations.  
**Recommendations:** Block known Railway ranges if business use allows; require compliant devices for Exchange Online and SharePoint; enable Continuous Access Evaluation and monitor for `BAV2ROPC` and anomalous non-interactive sign-ins.  
**Source:** [Riding the Rails: Threat Actors Abuse Railway.com PaaS as Microsoft 365 Token Attack Infrastructure](https://www.huntress.com/blog/railway-paas-m365-token-replay-campaign?adgroupid=2467031691897912247&adid=2467031691899043654&campaignid=2409163871146438346&clickID=6102520626130835999&hnt=dvndno2nzrji&rdt_cid=6102520626130835999&utm_campaign=reddit-tofu-traffic-solutions&utm_content=Reddit-ToFu-Traffic-Solutions-EMEA-KWSubreddits-Image-SelfFailsAi&utm_medium=paidsocial&utm_source=reddit)

### SharePoint-based AiTM phishing and BEC expansion
**Type:** AiTM phishing / business email compromise  
**Severity:** Critical  
**MITRE ATT&CK:** T1566.002, T1528, T1114, T1098  
**CVEs:** None  
**Affected:** Microsoft 365, SharePoint Online, Exchange Online, Microsoft Entra ID  
**M365/Azure relevance:** Attackers abused SharePoint sharing workflows, session theft, and mailbox manipulation inside Microsoft 365.  
**Summary:** Microsoft documented a multi-stage campaign in which attackers used a compromised trusted sender and SharePoint lures to steal sessions, create inbox rules that hid incoming mail, and then launch large-scale internal and external phishing from victim accounts. The activity escalated into BEC, with attackers reading responses, deleting warnings, and maintaining persistence beyond simple credential theft.  
**Recommendations:** Revoke session cookies, not just passwords; hunt for inbox-rule creation and abnormal email deletion; apply conditional access and phishing-resistant MFA to high-risk users.  
**Source:** [Resurgence of a multi-stage AiTM phishing and BEC campaign abusing SharePoint](https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/)

### OAuth abuse against SaaS tenants with downstream identity risk
**Type:** OAuth abuse / consent phishing / SaaS data theft  
**Severity:** High  
**MITRE ATT&CK:** T1566.004, T1528, T1671, T1213.004, T1567  
**CVEs:** None  
**Affected:** Salesforce, connected SaaS applications, federated enterprise identities  
**M365/Azure relevance:** The same OAuth abuse patterns, consent abuse, and app-governance gaps map directly to Entra-connected SaaS estates and Microsoft 365 app governance.  
**Summary:** Microsoft tied ShinyHunters-linked activity to vishing-driven OAuth consent abuse, third-party SaaS compromise, and guest-access misuse. Although the primary incidents centered on Salesforce, the operational lesson for Microsoft tenants is direct: trusted OAuth relationships and connected apps can provide persistence, sanctioned API access, and stealthy data theft without obvious sign-in anomalies.  
**Recommendations:** Review high-privilege app consents and stale app registrations; tighten non-human identity governance and guest access; use Defender for Cloud Apps and Entra app-governance controls to monitor abnormal OAuth activity.  
**Source:** [Defending SaaS-based applications against ShinyHunters OAuth abuse](https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/)

### Email threat activity: Tycoon2FA, QR phishing, CAPTCHA evasion, and BEC
**Type:** Phishing / PhaaS / business email compromise  
**Severity:** High  
**MITRE ATT&CK:** T1566, T1528, T1114, T1583  
**CVEs:** None  
**Affected:** Exchange Online, Microsoft Defender for Office 365, Microsoft 365 identities  
**M365/Azure relevance:** Microsoft measured large-scale targeting of enterprise mail users, including AiTM phishing and device code phishing trends relevant to Microsoft 365 tenants.  
**Summary:** Microsoft reported 8.3 billion email-based phishing threats in Q1 2026 and 10.7 million BEC attacks, with QR phishing more than doubling during the quarter. Tycoon2FA activity dropped after disruption but adapted infrastructure, while Microsoft also flagged emerging device-code phishing and persistent low-effort BEC outreach that can lead to fraud and mailbox compromise.  
**Recommendations:** Enforce Safe Links, Safe Attachments, ZAP, and anti-phishing policies; drill users on QR, CAPTCHA, and “verify to view document” lures; prioritize detection of post-click risky sign-ins and mailbox-rule abuse.  
**Source:** [Email threat landscape: Q1 2026 trends and insights](https://www.microsoft.com/en-us/security/blog/2026/04/30/email-threat-landscape-q1-2026-trends-and-insights/)

### ACR Stealer campaigns targeting browser tokens and Microsoft 365 data
**Type:** Infostealer / post-compromise credential theft  
**Severity:** High  
**MITRE ATT&CK:** T1059.001, T1218.011, T1218.005, T1053.005, T1555.003  
**CVEs:** None  
**Affected:** Windows endpoints, Microsoft Edge, Chromium browsers, OneDrive, SharePoint, Microsoft 365 documents  
**M365/Azure relevance:** The malware explicitly targets browser tokens and Microsoft 365 documents in synced enterprise locations such as OneDrive and SharePoint.  
**Summary:** Microsoft observed two ACR Stealer intrusion chains using ClickFix, WebDAV, `rundll32`, `mshta`, PowerShell, and in-memory payload delivery. Beyond browser credential theft, the campaigns specifically enumerated and staged Microsoft 365 documents and enterprise-synced data, creating direct follow-on risk to cloud identities and collaboration content.  
**Recommendations:** Block or constrain `mshta`, `rundll32`, and untrusted PowerShell execution; investigate DPAPI activity and browser-store access; rotate exposed tokens and review OneDrive and SharePoint access after endpoint compromise.  
**Source:** [ACR Stealer: Two observed intrusion chains amid increased threat activity](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/)

### GigaWiper destructive backdoor with ransomware-style impact
**Type:** Wiper / destructive malware / ransomware-like impact  
**Severity:** High  
**MITRE ATT&CK:** T1485, T1486, T1053.005, T1071  
**CVEs:** None  
**Affected:** Windows endpoints, hybrid enterprise environments, cloud-connected operations  
**M365/Azure relevance:** While not M365-specific, the malware poses high impact to hybrid enterprises by destroying endpoints, disrupting operations, and degrading cloud access paths and recovery workflows.  
**Summary:** Microsoft described GigaWiper as a modular backdoor that combines disk wiping, fake-ransomware file destruction, persistence, and remote control. For Microsoft-centric environments, the relevance is operational: destructive endpoint activity can sever access to Microsoft 365, destroy synchronized data paths, and complicate response in hybrid or cloud-dependent environments.  
**Recommendations:** Enable tamper protection and EDR block mode; isolate infected hosts quickly and hunt for scheduled-task persistence; prioritize offline recovery paths for identity administration and critical cloud-connected endpoints.  
**Source:** [GigaWiper: Anatomy of a destructive backdoor assembled from multiple malware](https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/)

## Threat Actor Activity
Storm-2372 remains a key identity threat for Microsoft tenants because it uses device code phishing and Microsoft Graph access to steal tokens, search mail, and exfiltrate sensitive data. EvilTokens-linked operators appear to have industrialized the same tradecraft with Railway-hosted automation, varied lures, and large-scale targeting. Storm-1747 and the Tycoon2FA ecosystem continue to matter because AiTM phishing, CAPTCHA evasion, and hosted credential theft remain active despite disruption. Microsoft also linked ShinyHunters-related activity to OAuth abuse and trusted SaaS integrations, reinforcing that identity compromise increasingly happens through app trust and token misuse rather than password guessing alone.

## Recommended Actions
1. Block or tightly scope device code flow in Entra ID and require explicit exceptions for approved use cases.
2. Require phishing-resistant MFA for privileged, executive, finance, and admin roles; pair it with conditional access and Continuous Access Evaluation.
3. Hunt for token-theft indicators across Entra, Exchange Online, SharePoint, and Graph activity, including risky sign-ins, suspicious non-interactive token use, inbox-rule creation, and anomalous `MailItemsAccessed`.
4. Review OAuth app consents, service principals, guest access, and non-human identities for excessive privileges, stale access, or unexplained recent changes.
5. Strengthen Defender for Office 365 controls against QR phishing, CAPTCHA-gated lures, malicious HTML/PDF attachments, and post-delivery campaign cleanup.
6. Prepare response playbooks that revoke refresh tokens, invalidate sessions, remove inbox rules, and investigate downstream SharePoint, OneDrive, and Graph access after any identity compromise.
7. Harden endpoints against ClickFix, browser-token theft, and destructive malware by restricting risky scripting binaries, enabling tamper protection, and validating recovery paths for Microsoft 365-dependent operations.

## Sources
- [Inside an AI-enabled device code phishing campaign](https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/)
- [Riding the Rails: Threat Actors Abuse Railway.com PaaS as Microsoft 365 Token Attack Infrastructure](https://www.huntress.com/blog/railway-paas-m365-token-replay-campaign?adgroupid=2467031691897912247&adid=2467031691899043654&campaignid=2409163871146438346&clickID=6102520626130835999&hnt=dvndno2nzrji&rdt_cid=6102520626130835999&utm_campaign=reddit-tofu-traffic-solutions&utm_content=Reddit-ToFu-Traffic-Solutions-EMEA-KWSubreddits-Image-SelfFailsAi&utm_medium=paidsocial&utm_source=reddit)
- [Resurgence of a multi-stage AiTM phishing and BEC campaign abusing SharePoint](https://www.microsoft.com/en-us/security/blog/2026/01/21/multistage-aitm-phishing-bec-campaign-abusing-sharepoint/)
- [Defending SaaS-based applications against ShinyHunters OAuth abuse](https://www.microsoft.com/en-us/security/blog/2026/07/13/defending-saas-based-applications-against-shinyhunters-oauth-abuse/)
- [Email threat landscape: Q1 2026 trends and insights](https://www.microsoft.com/en-us/security/blog/2026/04/30/email-threat-landscape-q1-2026-trends-and-insights/)
- [ACR Stealer: Two observed intrusion chains amid increased threat activity](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/)
- [GigaWiper: Anatomy of a destructive backdoor assembled from multiple malware](https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/)
- [Storm-2372 conducts device code phishing campaign](https://www.microsoft.com/en-us/security/blog/2025/02/13/storm-2372-conducts-device-code-phishing-campaign/)
