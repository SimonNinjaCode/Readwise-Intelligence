# Threat Intelligence Report — 2026-07-06

## Executive Summary
AiTM phishing remains the most immediate Microsoft 365 and Entra ID risk in this reporting set, driven by Tycoon2FA, multi-stage token-stealing phishing, and sustained growth in QR code, CAPTCHA-gated, and BEC delivery patterns. The most critical issue is continued session theft that bypasses non-phishing-resistant MFA and gives attackers live access to Microsoft 365 identities, mailboxes, and cloud applications.

## Key Threats

### Tycoon2FA AiTM phishing at scale
**Type:** AiTM phishing / session theft
**Severity:** Critical
**MITRE ATT&CK:** T1566.001, T1557, T1539
**CVEs:** None
**Affected:** Microsoft 365, Outlook, OneDrive, SharePoint, Microsoft Entra ID users
**M365/Azure relevance:** Tycoon2FA impersonates Microsoft sign-in flows, steals session cookies, and can retain access to Microsoft 365 accounts after password reset unless sessions and tokens are revoked.
**Summary:** Microsoft reported that Storm-1747’s Tycoon2FA platform enabled large-scale phishing against Microsoft 365 users with MFA interception, token theft, QR-code and attachment-based lures, and rapid domain rotation. Follow-on reporting shows the March 2026 disruption reduced activity, but the infrastructure adapted rather than disappearing.
**Recommendations:** Require phishing-resistant MFA for privileged and high-risk users; enforce token/session revocation during incident response; enable Safe Links, Safe Attachments, and network protection for time-of-click coverage.
**Source:** Inside Tycoon2FA: How a leading AiTM phishing kit operated at scale — https://www.microsoft.com/en-us/security/blog/2026/03/04/inside-tycoon2fa-how-a-leading-aitm-phishing-kit-operated-at-scale/

### Code-of-conduct phishing leading to token compromise
**Type:** Targeted phishing / AiTM token theft
**Severity:** High
**MITRE ATT&CK:** T1566.001, T1557, T1539
**CVEs:** None
**Affected:** Microsoft 365 accounts, Entra ID sign-ins, Outlook-delivered mail
**M365/Azure relevance:** The campaign ended on a “Sign in with Microsoft” flow designed to proxy authentication and steal tokens for Microsoft accounts.
**Summary:** Between April 14 and 16, 2026, Microsoft observed a large phishing campaign targeting more than 35,000 users across 13,000 organizations. Attackers used PDF attachments, multiple CAPTCHA stages, and intermediate pages before routing targets into an AiTM flow that captured authentication tokens despite MFA.
**Recommendations:** Hunt for campaign domains and attachment hashes in Defender for Office 365; prioritize passwordless or phishing-resistant MFA for browser-based sign-ins; alert on anomalous token use and risky sign-ins immediately after malicious URL clicks.
**Source:** Breaking the code: Multi-stage ‘code of conduct’ phishing campaign leads to AiTM token compromise — https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/

### QR-code phishing, CAPTCHA-gated phishing, and BEC growth
**Type:** Phishing / BEC / credential theft
**Severity:** High
**MITRE ATT&CK:** T1566.001, T1566.002
**CVEs:** None
**Affected:** Exchange Online, Microsoft 365 mail users, finance and payroll workflows
**M365/Azure relevance:** Exchange Online remains the delivery path; Microsoft 365 users are targeted through email attachments, sign-in lures, and BEC pretexts that can lead to account compromise and payment fraud.
**Summary:** Microsoft counted 8.3 billion phishing threats in Q1 2026. QR-code phishing more than doubled, CAPTCHA-gated phishing more than doubled in March, and BEC stayed persistent at 10.7 million attacks, with Tycoon2FA, Kratos, and EvilTokens-linked infrastructure appearing in major campaigns.
**Recommendations:** Tighten Exchange Online and Defender for Office 365 recommended settings; use ZAP, Safe Links, and Safe Attachments broadly; harden finance and payroll approval workflows against conversational BEC.
**Source:** Email threat landscape: Q1 2026 trends and insights — https://www.microsoft.com/en-us/security/blog/2026/04/30/email-threat-landscape-q1-2026-trends-and-insights/

### Jasper Sleet remote IT worker infiltration
**Type:** Identity fraud / insider-style access abuse
**Severity:** High
**MITRE ATT&CK:** T1078, T1078.004, T1585
**CVEs:** None
**Affected:** Workday, Microsoft Teams, SharePoint, OneDrive, Exchange Online, newly provisioned Entra-backed user accounts
**M365/Azure relevance:** The threat becomes material after onboarding, when the actor receives legitimate access to Microsoft 365 services and can operate under trusted identity.
**Summary:** Microsoft described how Jasper Sleet uses fake or stolen identities, HR SaaS workflows, and post-hire onboarding activity to gain trusted enterprise access. Once onboarded, the actor can access Microsoft 365 collaboration and data stores while blending in as a new employee.
**Recommendations:** Correlate HR, identity, and M365 telemetry for new hires; investigate impossible travel and suspicious payroll or onboarding changes tied to new accounts; review external recruiting and interview workflows for known Jasper Sleet indicators.
**Source:** Detection strategies across cloud and identities against infiltrating IT workers — https://www.microsoft.com/en-us/security/blog/2026/04/21/detection-strategies-cloud-identities-against-infiltrating-it-workers/

### Threat actors operationalizing AI for phishing, impersonation, and BEC
**Type:** AI-enabled social engineering / access abuse
**Severity:** High
**MITRE ATT&CK:** T1566, T1585, T1078
**CVEs:** None
**Affected:** Microsoft 365 users, Entra identities, HR and collaboration workflows
**M365/Azure relevance:** Microsoft links AI-enabled lure generation, fake identity creation, and long-term access abuse directly to M365-facing phishing, BEC, and insider-style compromise scenarios.
**Summary:** Microsoft assessed that threat actors are using AI to improve phishing content, fake identities, infrastructure setup, and post-compromise decision support. Jasper Sleet and Coral Sleet were cited as concrete examples of AI-assisted identity fraud, social engineering, and persistence that increase pressure on Microsoft 365 and Entra defenses.
**Recommendations:** Treat AI-assisted identity fraud as an insider-risk problem; strengthen phishing-resistant MFA and user verification for sensitive workflows; monitor for anomalous use of new AI apps and suspicious prompt or content-safety signals in Azure AI and Defender telemetry.
**Source:** AI as tradecraft: How threat actors operationalize AI — https://www.microsoft.com/en-us/security/blog/2026/03/06/ai-as-tradecraft-how-threat-actors-operationalize-ai/

### Hybrid identity attack chain from Azure-hosted edge appliance compromise
**Type:** Hybrid intrusion / credential theft / relay attack
**Severity:** High
**MITRE ATT&CK:** T1190, T1021.004, T1187, T1557
**CVEs:** CVE-2025-53521, CVE-2025-33073
**Affected:** Azure-hosted F5 BIG-IP, Confluence, Active Directory, hybrid identity infrastructure
**M365/Azure relevance:** The incident started on an Azure-hosted F5 appliance and escalated into credential theft and relay activity against domain services that commonly underpin hybrid Microsoft identity estates.
**Summary:** Microsoft documented a multi-stage intrusion that began with an Azure-hosted, end-of-life F5 BIG-IP appliance, pivoted to Linux and Confluence systems, and ended in credential theft and relay-style attacks against Windows identity infrastructure. The case is a reminder that Azure-connected edge systems and internal apps can become stepping stones into Microsoft identity environments.
**Recommendations:** Treat internet-facing Azure-hosted appliances as Tier-0 assets; patch internal applications with the same urgency as external systems; reduce relay paths with SMB signing, LDAP signing, EPA, and privileged account separation.
**Source:** From edge appliance to enterprise compromise: Multi-stage Linux intrusion via F5 and Confluence — https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/

## Threat Actor Activity
Storm-1747 remained the most relevant named actor in this set through Tycoon2FA operations and broader AiTM phishing activity against Microsoft 365 users. Jasper Sleet remained active in identity-centric operations, combining fake personas, HR workflow abuse, and legitimate post-hire access. Microsoft also tied Coral Sleet and Emerald Sleet to AI-enabled tradecraft that improves phishing, persona development, and exploit research.

## Recommended Actions
Prioritize phishing-resistant MFA for privileged users, executives, finance, HR, and all externally exposed Microsoft 365 workflows.
Revoke active sessions and refresh tokens as a standard response step for suspected AiTM compromise, not just password resets.
Expand Defender for Office 365 protections with Safe Links, Safe Attachments, ZAP, and mailbox hunting for QR-code, PDF, HTML, and SVG lure chains.
Correlate HR, Entra, Exchange Online, Teams, SharePoint, and Workday signals for new hires and external recruiting activity.
Harden hybrid identity paths by reducing NTLM and relay exposure, enforcing SMB and LDAP protections, and patching Azure-hosted edge appliances and internal web apps on an accelerated cycle.

## Sources
Inside Tycoon2FA: How a leading AiTM phishing kit operated at scale — https://www.microsoft.com/en-us/security/blog/2026/03/04/inside-tycoon2fa-how-a-leading-aitm-phishing-kit-operated-at-scale/
Breaking the code: Multi-stage ‘code of conduct’ phishing campaign leads to AiTM token compromise — https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/
Email threat landscape: Q1 2026 trends and insights — https://www.microsoft.com/en-us/security/blog/2026/04/30/email-threat-landscape-q1-2026-trends-and-insights/
Detection strategies across cloud and identities against infiltrating IT workers — https://www.microsoft.com/en-us/security/blog/2026/04/21/detection-strategies-cloud-identities-against-infiltrating-it-workers/
AI as tradecraft: How threat actors operationalize AI — https://www.microsoft.com/en-us/security/blog/2026/03/06/ai-as-tradecraft-how-threat-actors-operationalize-ai/
From edge appliance to enterprise compromise: Multi-stage Linux intrusion via F5 and Confluence — https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/
