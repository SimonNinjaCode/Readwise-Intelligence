# Threat Intelligence Report — 2026-09-28

## Executive Summary

September’s material is dominated by identity abuse in Microsoft 365 and Azure: device-code phishing, token theft, Teams impersonation and compromised workload identities. The most serious case is Storm-3168, which used compromised Azure service principals to enumerate and destroy cloud resources; EvilTokens shows how the same identity layer can be industrialised into mass account compromise. Defenders should prioritise workload-identity governance, phishing-resistant authentication, device-code controls and rapid detection of abnormal Graph, Teams and Azure activity.

## Key Threats

### Storm-3168: destructive Azure operations through service principals
**Type:** Cloud identity compromise and resource destruction  
**Severity:** Critical  
**MITRE ATT&CK:** T1190, T1078.004, T1526, T1485, T1552.004  
**CVEs:** None reported  
**Affected:** Azure Storage, SQL databases, Key Vault, Function Apps, App Services, virtual machines and recovery controls  
**M365/Azure relevance:** Compromised service principals can operate outside normal user-centric monitoring and destroy or access Azure resources at scale.  
**Summary:** Microsoft linked JADEPUFFER to Storm-3168 and observed compromised service principals performing discovery, destructive actions and credential collection across Azure. The activity included resource deletion and attempts to retrieve storage keys.  
**Recommendations:** Remove standing Global Administrator and broad resource roles from workload identities; rotate exposed secrets and certificates; protect recovery resources with independent controls and alert on bulk service-principal discovery or deletion.  
**Source:** [Storm-3168: Agentic-driven cloud attacks using compromised service principals](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)

### EvilTokens and device-code phishing
**Type:** OAuth device-code phishing and token theft  
**Severity:** Critical  
**MITRE ATT&CK:** T1566, T1566.002, T1078.004, T1528, T1098  
**CVEs:** None reported  
**Affected:** Microsoft Entra ID, Microsoft 365 mailboxes, Teams devices and Microsoft Graph  
**M365/Azure relevance:** Valid device-code authentication is being abused to obtain cloud tokens without stealing a password.  
**Summary:** Microsoft tracked the EvilTokens operation to Storm-2992. The platform supported automated phishing, token theft, mailbox reconnaissance and Graph-based organisational mapping; related reporting describes more than 12,000 compromised inboxes across over 10,000 organisations.  
**Recommendations:** Disable or restrict device-code flow where it is not required; require phishing-resistant authentication and compliant devices; alert on unusual device-code sign-ins, new authentication methods, high-volume Graph access and mailbox collection.  
**Source:** [Unmasking EvilTokens: Getting to the root of device code phishing](https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/)

### Passkey-themed social engineering and cloud takeover
**Type:** Phishing, session/token theft and persistence  
**Severity:** Critical  
**MITRE ATT&CK:** T1598.003, T1566.003, T1528, T1098.005, T1114  
**CVEs:** None reported  
**Affected:** Entra ID, Microsoft 365, Teams, SharePoint, OneDrive and connected SaaS applications  
**M365/Azure relevance:** A compromised cloud identity can be used to register new MFA methods, search tenant data, collect mail and access Graph APIs.  
**Summary:** Microsoft described active intrusions using passkey, SSO and account-verification lures. After initial access, actors added authentication methods and performed Graph, SharePoint, OneDrive and mailbox reconnaissance.  
**Recommendations:** Alert on authentication-method changes and risky Graph enumeration; require phishing-resistant authentication bound to managed devices; review OAuth grants, application permissions and anomalous downloads after a suspicious sign-in.  
**Source:** [Passkey-themed social engineering leads to identity and cloud compromise](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/)

### Teams helpdesk impersonation
**Type:** Spearphishing via service, remote access and hands-on-keyboard intrusion  
**Severity:** High  
**MITRE ATT&CK:** T1566.003, T1219, T1059.001, T1218.007, T1021.006, T1105  
**CVEs:** None reported  
**Affected:** Microsoft Teams external collaboration, Windows endpoints, PowerShell, RMM tools and identity systems  
**M365/Azure relevance:** External Teams contact can become the initial access path into a tenant and a route to identity infrastructure.  
**Summary:** Threat actors impersonated IT support through external Teams chats or calls, persuaded users to grant remote control, then installed MSI and JavaScript tooling and moved towards identity systems.  
**Recommendations:** Restrict external Teams communication and federation; train staff that helpdesk never requests unsolicited remote control; hunt for RMM installation followed by PowerShell, WinRM and identity-system discovery.  
**Source:** [Impersonating IT support: how threat actors turn a remote session into enterprise-wide access](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)

### ASCII smuggling in phishing
**Type:** Phishing evasion and content obfuscation  
**Severity:** High  
**MITRE ATT&CK:** T1566, T1027  
**CVEs:** None reported  
**Affected:** Exchange Online, Microsoft Defender for Office 365 and AI assistants processing email  
**M365/Azure relevance:** Invisible Unicode characters can alter what classifiers and AI systems see while leaving the message readable to a human.  
**Summary:** Microsoft observed ASCII smuggling moving from AI prompt-injection research into phishing campaigns. The technique hides lure terms from filters and can also manipulate downstream AI processing.  
**Recommendations:** Normalise and inspect Unicode in mail pipelines; use Defender for Office 365 detections and hunting for tag-block characters; apply the same input validation to AI assistants that ingest email or documents.  
**Source:** [ASCII smuggling crosses over from AI prompt injection to phishing evasion](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/)

### Storm-2570 ransomware tradecraft
**Type:** Human-operated intrusion and ransomware  
**Severity:** High  
**MITRE ATT&CK:** T1059.001, T1021.001, T1021.002, T1562.001, T1078, T1486  
**CVEs:** None specified in the article  
**Affected:** Windows endpoints, remote-access infrastructure, identity systems and file servers  
**M365/Azure relevance:** The recurring identity, remote-access and security-tampering stages provide detection opportunities before ransomware deployment.  
**Summary:** Microsoft linked Storm-2570 activity across multiple ransomware ecosystems. The actor repeatedly used remote access, credential access, lateral movement, security tampering, exfiltration and ransomware deployment.  
**Recommendations:** Enable Defender attack surface reduction rules; monitor remote-access tools, LSASS access and security-control changes; correlate identity, endpoint and network telemetry before impact occurs.  
**Source:** [Beyond the ransomware: Tracking Storm-2570’s consistent tradecraft across deployments](https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/)

### Counterfeit installers and Defender tampering
**Type:** Malicious software delivery, persistence and defence evasion  
**Severity:** High  
**MITRE ATT&CK:** T1204.002, T1059.001, T1059.003, T1218.007, T1053.005, T1562.001, T1490  
**CVEs:** None reported  
**Affected:** Windows endpoints, Microsoft Defender, Windows Update and recovery services  
**M365/Azure relevance:** Endpoint compromise can become a cloud compromise when browser sessions, credentials or tokens are present on the device.  
**Summary:** A deceptive download campaign used spoofed software pages, scheduled tasks, signed binaries and Defender exclusions. The payload disabled security and recovery controls and used rotating infrastructure.  
**Recommendations:** Enforce Defender Tamper Protection; block or restrict unsigned and unexpected installers; hunt for Add-MpPreference, scheduled tasks, shadow-copy deletion and trusted binaries launched from user-writable paths.  
**Source:** [Counterfeit installers to system compromise: Tracking a deceptive software download campaign](https://www.microsoft.com/en-us/security/blog/2026/09/01/counterfeit-installers-system-compromise-tracking-deceptive-software-download-campaign/)

### Identity posture gaps in SaaS and Entra
**Type:** Privilege abuse and valid-account compromise  
**Severity:** High  
**MITRE ATT&CK:** T1078.004, T1098, T1098.003, T1531  
**CVEs:** None reported  
**Affected:** Entra ID, SaaS-native administrator accounts, service accounts, guests and sensitive groups  
**M365/Azure relevance:** Accounts outside IdP control, excessive service-account privilege and delegated directory permissions bypass normal Conditional Access and governance.  
**Summary:** Microsoft’s ISPM recommendations target privileged SaaS accounts outside the IdP, overprivileged service identities, shadow password-reset rights, WriteDACL exposure and privileged guest accounts.  
**Recommendations:** Bring SaaS administrators under federated identity; remove Global Administrator and Domain Admin assignments from service accounts; review delegated permissions, guest roles, dormant privileged accounts and browser-session persistence.  
**Source:** [Stop identity attacks before they start with Microsoft ISPM recommendations](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/stop-identity-attacks-before-they-start-with-microsoft-ispm/ba-p/4549692)

## Threat Actor Activity

- Storm-3168, also known as JADEPUFFER, used compromised Azure service principals for discovery, destructive operations and credential collection.
- Storm-2992 operated and supported the EvilTokens device-code phishing service.
- Storm-2570 continued a cross-deployment ransomware tradecraft pattern involving remote access, credential access, lateral movement and security tampering.
- Storm-2945, a Midnight Blizzard subcluster, was referenced in Microsoft’s September guidance on captive-network redirection, device-code phishing and fake software updates.
- ClickFix operators continued to use user-executed commands and fake troubleshooting or update workflows across Windows and macOS.

## Recommended Actions

1. Disable or constrain Entra device-code authentication and require phishing-resistant MFA on privileged and high-risk access paths.
2. Inventory service principals, workload identities, OAuth grants and SaaS-native administrator accounts. Remove standing privilege, rotate secrets and alert on abnormal token use.
3. Review external Teams access and helpdesk procedures. Restrict unsolicited external contact and prohibit user-granted remote control without verified out-of-band approval.
4. Enable Defender Tamper Protection, ASR rules and Attack Disruption. Hunt for PowerShell, RMM, WinRM, scheduled-task persistence, Defender exclusions and shadow-copy deletion.
5. Build detections for authentication-method changes, device-code sign-ins, Graph enumeration, SharePoint/OneDrive collection and mailbox export after unusual sign-ins.
6. Normalise Unicode in mail and AI ingestion pipelines, and use Defender for Office 365 hunting for ASCII-smuggling indicators.
7. Protect Azure recovery resources separately from ordinary administrator permissions and alert on bulk service-principal discovery, key retrieval or resource deletion.

## Sources

- [Entra 🆔 News #168 — This week in Microsoft Entra](https://entra.news/p/entra-news-168-this-week-in-microsoft)
- [Storm-3168: Agentic-driven cloud attacks using compromised service principals](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)
- [Beyond the ransomware: Tracking Storm-2570’s consistent tradecraft across deployments](https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/)
- [Microsoft disrupts AI-assisted platform that compromised 12,000](https://arstechnica.com/security/2026/09/microsoft-disrupts-ai-assisted-platform-that-compromised-12000/)
- [Unmasking EvilTokens: Getting to the root of device code phishing](https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/)
- [How to track browser extension installations with Microsoft Defender](https://jeffreyappel.nl/how-to-track-browser-extension-installations-with-microsoft-defender/)
- [Improving email security outcomes with real-world Microsoft Defender insights](https://www.microsoft.com/en-us/security/blog/2026/09/17/improving-email-security-outcomes-with-real-world-microsoft-defender-insights/)
- [From guidance to action: Security fundamentals that materially reduce risk](https://www.microsoft.com/en-us/security/blog/2026/09/17/from-guidance-to-action-security-fundamentals-that-materially-reduce-risk/)
- [ClickFix attacks infecting PCs and Macs are going viral](https://arstechnica.com/security/2026/09/clickfix-attacks-infecting-pcs-and-macs-are-going-viral/)
- [Detect and disrupt AI-themed attacks with Microsoft Defender](https://www.microsoft.com/en-us/security/blog/2026/09/10/detect-and-disrupt-ai-themed-attacks-with-microsoft-defender/)
- [Protecting organizations from AI-assisted executive impersonation and invoice fraud](https://www.microsoft.com/en-us/security/blog/2026/09/10/protecting-organizations-ai-assisted-executive-impersonation-invoice-fraud/)
- [Threat matrix: Mapping threats across cloud web applications](https://www.microsoft.com/en-us/security/blog/2026/09/09/threat-matrix-mapping-threats-across-cloud-web-applications/)
- [Microsoft Defender XDR Attack Disruption: Automatic Device Isolation Explained](https://jeffreyappel.nl/microsoft-defender-xdr-attack-disruption-automatic-device-isolation-explained/)
- [Passkey-themed social engineering leads to identity and cloud compromise](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/)
- [Once popular for attacking AI, ASCII smuggling is embraced by spammers](https://arstechnica.com/security/2026/09/once-popular-for-attacking-ai-ascii-smuggling-is-embraced-by-spammers/)
- [ASCII smuggling crosses over from AI prompt injection to phishing evasion](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/)
- [Impersonating IT support: how threat actors turn a remote session into enterprise-wide access](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)
- [Counterfeit installers to system compromise: Tracking a deceptive software download campaign](https://www.microsoft.com/en-us/security/blog/2026/09/01/counterfeit-installers-system-compromise-tracking-deceptive-software-download-campaign/)
- [Stop identity attacks before they start with Microsoft ISPM recommendations](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/stop-identity-attacks-before-they-start-with-microsoft-ispm/ba-p/4549692)
