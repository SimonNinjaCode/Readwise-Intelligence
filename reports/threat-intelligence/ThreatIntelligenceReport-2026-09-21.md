# Threat Intelligence Report — 2026-09-21

## Executive Summary

September reporting is dominated by identity abuse, trusted-channel social engineering, and user-assisted malware delivery. The most serious M365 risk is the passkey-themed campaign that establishes MFA persistence, abuses Microsoft Graph for reconnaissance, and reaches SharePoint, OneDrive, and email; TeamPCP’s supply-chain activity adds a separate route to stolen credentials and cloud access.

## Key Threats

### Passkey-themed identity and cloud compromise
**Type:** Identity phishing, MFA persistence, cloud data theft  
**Severity:** Critical  
**MITRE ATT&CK:** T1566.002, T1098.005, T1528, T1087.004, T1213  
**CVEs:** None reported  
**Affected:** Microsoft Entra ID, Microsoft Graph, SharePoint, OneDrive, Exchange Online  
**M365/Azure relevance:** Direct. The campaign uses a passkey lure to compromise identities, add authentication persistence, enumerate tenants, and access cloud data.  
**Summary:** Microsoft observed social engineering themed around passkeys followed by MFA persistence, Graph reconnaissance, and access to SharePoint, OneDrive, and email. Phishing-resistant authentication reduces exposure, but recovery paths and newly registered methods remain high-value controls.  
**Recommendations:** Review newly registered authentication methods and suspicious OAuth or session activity. Alert on unusual Graph enumeration and cross-service access. Tighten privileged recovery and authentication-method registration controls.  
**Source:** [Passkey-themed social engineering leads to identity and cloud compromise](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/)

### TeamPCP supply-chain compromise and credential theft
**Type:** Software supply-chain compromise, credential theft, account takeover  
**Severity:** Critical  
**MITRE ATT&CK:** T1195.002, T1552.001, T1552.004, T1539  
**CVEs:** None reported in the article  
**Affected:** Open-source packages, GitHub, CI/CD pipelines, developer identities, AWS and Microsoft-hosted services  
**M365/Azure relevance:** High. Stolen developer credentials and access tokens can reach Azure subscriptions, Microsoft integrations, repositories, and automation identities.  
**Summary:** TeamPCP compromised hundreds of open-source projects, stole developer accounts, and accumulated more than half a million credentials. Google reported that it revoked stolen credentials through providers including Microsoft and disrupted an attempted zero-day operation linked to the group.  
**Recommendations:** Inventory package and CI exposure, revoke and rotate credentials reachable from compromised developer environments, and replace static secrets with short-lived workload identities. Review sign-ins and token use for developer and automation accounts.  
**Source:** [An undercover Google analyst infiltrated a notorious supply-chain hacking gang](https://arstechnica.com/security/2026/09/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/)

### Teams helpdesk impersonation
**Type:** Social engineering, remote access, lateral movement  
**Severity:** High  
**MITRE ATT&CK:** T1566.003, T1656, T1219, T1021.006, T1078  
**CVEs:** None reported  
**Affected:** Microsoft Teams external collaboration, Windows endpoints, Active Directory, remote support tooling  
**M365/Azure relevance:** Direct. Attackers use external Teams contact to impersonate IT support, obtain interactive remote access, deploy a Node.js implant, and pivot toward domain controllers.  
**Summary:** The campaign moves from Teams contact to remote-support approval, PowerShell, a malicious MSI, and hands-on-keyboard activity. Legitimate tools and administrative protocols make the intrusion difficult to distinguish from support work without cross-surface correlation.  
**Recommendations:** Restrict external Teams communication where it is not required. Require verified internal workflows for remote support. Hunt for Teams contact followed by remote-assistance tools, PowerShell, MSI installation, Node.js execution, or WinRM.  
**Source:** [Impersonating IT support: how threat actors turn a remote session into enterprise-wide access](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)

### AI-themed phishing and malvertising
**Type:** Brand impersonation, phishing, credential and payment theft  
**Severity:** High  
**MITRE ATT&CK:** T1566.002, T1583.001, T1584.004, T1189, T1204.002  
**CVEs:** None reported  
**Affected:** Microsoft 365 users, browsers, payment workflows, Defender for Office 365 and Defender for Endpoint  
**M365/Azure relevance:** Direct. AI product names are being used as high-trust lures that can begin in email, continue through redirects or downloads, and end in identity or endpoint compromise.  
**Summary:** Microsoft describes campaigns impersonating ChatGPT, Copilot, DeepSeek, and Claude. One ChatGPT-themed campaign sent up to 100,000 messages in a day to harvest payment details; the referenced AI services were not compromised.  
**Recommendations:** Treat AI-themed messages and downloads as a distinct phishing category. Correlate email, URL, browser, endpoint, and identity signals. Strengthen payment verification and block look-alike domains and high-risk redirect chains.  
**Source:** [Detect and disrupt AI-themed attacks with Microsoft Defender](https://www.microsoft.com/en-us/security/blog/2026/09/10/detect-and-disrupt-ai-themed-attacks-with-microsoft-defender/)

### AI-assisted executive impersonation and invoice fraud
**Type:** Business email compromise, payment fraud  
**Severity:** High  
**MITRE ATT&CK:** T1566.002, T1583.001, T1585.002, T1036.002, T1656  
**CVEs:** None reported  
**Affected:** Exchange Online, finance teams, accounts-payable workflows, third-party mail infrastructure  
**M365/Azure relevance:** Direct. The campaign uses look-alike domains, spoofed executives, fabricated service-desk threads, and ACH payment requests.  
**Summary:** Microsoft observed more than one million messages in an AI-assisted impersonation campaign targeting finance staff with personalized CEO lures and fake invoices. Header, display-name, and thread inconsistencies still provide useful detection signals.  
**Recommendations:** Enforce out-of-band payment verification and dual approval. Tune Defender for Office 365 for look-alike domains, display-name mismatch, and payment lures. Protect executive and finance identities with phishing-resistant authentication.  
**Source:** [Protecting organizations from AI-assisted executive impersonation and invoice fraud](https://www.microsoft.com/en-us/security/blog/2026/09/10/protecting-organizations-ai-assisted-executive-impersonation-invoice-fraud/)

### ClickFix and user-assisted execution
**Type:** Social engineering, command execution, malware delivery  
**Severity:** High  
**MITRE ATT&CK:** T1204.002, T1059.001, T1059.004, T1218, T1090.001  
**CVEs:** None reported  
**Affected:** Windows and macOS endpoints, browsers, PowerShell, Windows Run, macOS Terminal  
**M365/Azure relevance:** High. Compromised endpoints can expose browser sessions, credentials, refresh tokens, and access to M365 tenants.  
**Summary:** ClickFix lures persuade users to paste commands into trusted shells after passing a fake CAPTCHA or similar prompt. The technique is spreading across Windows and macOS because the user performs the execution step with normal privileges and trusted tools.  
**Recommendations:** Detect browser-to-shell and clipboard-to-shell execution. Apply Defender for Endpoint attack-surface reduction and script controls across Windows and macOS. Monitor for reverse tunnels, unusual shell ancestry, and token access after user-assisted execution.  
**Source:** [ClickFix attacks infecting PCs and Macs are going viral](https://arstechnica.com/security/2026/09/clickfix-attacks-infecting-pcs-and-macs-are-going-viral/)

### ASCII smuggling in phishing
**Type:** Defense evasion, phishing  
**Severity:** High  
**MITRE ATT&CK:** T1027, T1566.001  
**CVEs:** None reported  
**Affected:** Email clients, mail security gateways, Defender for Office 365  
**M365/Azure relevance:** Direct. Invisible Unicode characters can conceal words from filters while preserving the intended meaning for recipients and downstream systems.  
**Summary:** Microsoft reports that ASCII smuggling has moved from AI prompt-injection research into phishing. Attackers use invisible characters and confusables to reduce the value of simple keyword inspection.  
**Recommendations:** Normalize Unicode before content inspection and hunting. Test mail-flow rules against rendered-versus-raw text. Combine content analysis with sender authentication, URL reputation, and user behavior.  
**Source:** [ASCII smuggling crosses over from AI prompt injection to phishing evasion](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/)

### Counterfeit software installers
**Type:** Malware delivery, masquerading, persistence  
**Severity:** High  
**MITRE ATT&CK:** T1189, T1036.005, T1204.002, T1218  
**CVEs:** None reported  
**Affected:** Windows endpoints, software download workflows, Microsoft Defender XDR  
**M365/Azure relevance:** High. A compromised endpoint can expose browser sessions, credentials, and M365 tokens.  
**Summary:** Microsoft tracked look-alike download pages that impersonated trusted vendors and delivered regenerated installer archives. The campaign used persistence, defense evasion, and attacker-controlled infrastructure; Microsoft assessed it as consistent with Silver Fox activity with moderate confidence.  
**Recommendations:** Allow software installation from managed sources. Block or investigate newly registered look-alike domains and executables from user-writable paths. Keep SmartScreen, network protection, tamper protection, and Defender XDR enabled.  
**Source:** [Counterfeit installers to system compromise: Tracking a deceptive software download campaign](https://www.microsoft.com/en-us/security/blog/2026/09/01/counterfeit-installers-system-compromise-tracking-deceptive-software-download-campaign/)

### Identity posture gaps in SaaS and Entra environments
**Type:** Valid-account abuse, privilege escalation, persistence  
**Severity:** High  
**MITRE ATT&CK:** T1078.002, T1078.004, T1098, T1098.003  
**CVEs:** None reported  
**Affected:** Microsoft Entra ID, Active Directory, SaaS administrators, service accounts, guest identities  
**M365/Azure relevance:** Direct. Local SaaS admins, overprivileged service accounts, delegated password-reset rights, WriteDACL permissions, and privileged guests create paths around normal Conditional Access and monitoring.  
**Summary:** Microsoft’s new Identity Security Posture Management recommendations target identity weaknesses repeatedly used in real attacks. The common failure is not a missing feature; it is privileged access left outside the IdP, over-assigned, or invisible to the SOC.  
**Recommendations:** Bring SaaS administration under Entra federation and Conditional Access. Remove Global Admin or Domain Admin from service accounts. Review guest roles, password-reset rights, WriteDACL, dormant privileged accounts, and lateral-movement paths.  
**Source:** [Stop identity attacks before they start with Microsoft ISPM recommendations](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/stop-identity-attacks-before-they-start-with-microsoft-ispm/ba-p/4549692)

## Threat Actor Activity

TeamPCP remains the most consequential named actor in the selected material. Google described an undercover presence inside the group, its partnership with ShinyHunters, mass theft of credentials, and attempts to monetize or reuse those credentials. Microsoft attributes the Teams intrusion to a human-operated campaign without naming a group. The counterfeit-installer activity is assessed with moderate confidence as consistent with Silver Fox, while the AI-themed phishing and passkey campaigns are not publicly attributed to a named actor.

## Recommended Actions

1. Audit Entra authentication methods, refresh-token activity, risky sign-ins, OAuth grants, Graph enumeration, guest roles, and privileged service accounts.
2. Restrict Teams external access and require verified internal approval for remote support and high-risk administrative actions.
3. Tune Defender for Office 365 for AI-themed lures, executive impersonation, look-alike domains, Unicode obfuscation, payment fraud, and post-delivery remediation.
4. Hunt for browser-launched shells, clipboard-to-PowerShell or Terminal execution, reverse tunnels, MSI staging, Node.js implants, and WinRM from user context.
5. Enforce managed software acquisition and application control; block execution from user-writable and temporary paths.
6. Inventory package and CI/CD exposure, revoke compromised tokens, rotate secrets, and replace long-lived credentials with workload identities.
7. Test tenant and endpoint recovery paths without relying on ordinary production identities.

## Sources

- [An undercover Google analyst infiltrated a notorious supply-chain hacking gang](https://arstechnica.com/security/2026/09/an-undercover-google-analyst-infiltrated-a-notorious-supply-chain-hacking-gang/)
- [Passkey-themed social engineering leads to identity and cloud compromise](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/)
- [ClickFix attacks infecting PCs and Macs are going viral](https://arstechnica.com/security/2026/09/clickfix-attacks-infecting-pcs-and-macs-are-going-viral/)
- [Detect and disrupt AI-themed attacks with Microsoft Defender](https://www.microsoft.com/en-us/security/blog/2026/09/10/detect-and-disrupt-ai-themed-attacks-with-microsoft-defender/)
- [Protecting organizations from AI-assisted executive impersonation and invoice fraud](https://www.microsoft.com/en-us/security/blog/2026/09/10/protecting-organizations-ai-assisted-executive-impersonation-invoice-fraud/)
- [ASCII smuggling crosses over from AI prompt injection to phishing evasion](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/)
- [Impersonating IT support: how threat actors turn a remote session into enterprise-wide access](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)
- [Counterfeit installers to system compromise: Tracking a deceptive software download campaign](https://www.microsoft.com/en-us/security/blog/2026/09/01/counterfeit-installers-system-compromise-tracking-deceptive-software-download-campaign/)
- [Stop identity attacks before they start with Microsoft ISPM recommendations](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/stop-identity-attacks-before-they-start-with-microsoft-ispm/ba-p/4549692)
