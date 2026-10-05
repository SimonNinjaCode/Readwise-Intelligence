# Threat Intelligence Report — 2026-10-05

## Executive Summary

The primary October window contained limited M365-relevant threat material, so this report extends exactly one preceding month into September. The dominant risks were identity-led cloud compromise, Teams and remote-support abuse, phishing that steals tokens or deploys trusted remote-access tools, and destructive Azure activity through compromised service principals. The most immediate concern for Microsoft 365 environments is the convergence of social engineering, unauthorized authentication methods, Graph-based collection, and legitimate administration tools.

## Key Threats

### Identity compromise through passkey and device-code lures
**Type:** Adversary-in-the-middle phishing, device-code phishing, cloud account takeover  
**Severity:** Critical  
**MITRE ATT&CK:** T1566.002, T1528, T1098, T1078.004  
**CVEs:** None reported  
**Affected:** Microsoft Entra ID, Microsoft Graph, SharePoint, OneDrive, Exchange Online  
**M365/Azure relevance:** Attackers can add authentication methods, obtain session or access tokens, enumerate tenants through Graph, and collect files and email without deploying malware to endpoints.  
**Summary:** Microsoft observed campaigns using helpdesk and passkey narratives to drive victims through AiTM or device-code flows. Follow-on activity included attacker-added authentication methods, unusual sign-ins, Graph reconnaissance, SharePoint and OneDrive downloads, and email collection. EvilTokens provided a PhaaS capability for automated device-code phishing and token theft; Microsoft and partners disrupted its infrastructure.  
**Recommendations:** Require phishing-resistant authentication for privileged and high-risk users; alert on new authentication methods and unusual Graph or SharePoint collection; revoke sessions and remove unauthorized methods immediately after confirmed compromise.  
**Source:** [Passkey-themed social engineering leads to identity and cloud compromise](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/), [Unmasking EvilTokens: Getting to the root of device code phishing](https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/)

### Teams helpdesk impersonation and remote-session abuse
**Type:** Social engineering, remote-access abuse, lateral movement  
**Severity:** Critical  
**MITRE ATT&CK:** T1566.002, T1219, T1059.001, T1021.006, T1087.002  
**CVEs:** None reported  
**Affected:** Microsoft Teams external collaboration, Windows endpoints, Active Directory, remote administration tools  
**M365/Azure relevance:** External Teams messaging becomes the initial-access channel, while RMM, PowerShell, WinRM, and legitimate Windows tooling provide the path to domain controllers and other high-value assets.  
**Summary:** A human-operated campaign impersonated IT or helpdesk personnel in Teams and persuaded users to grant interactive remote sessions. The operators installed an obfuscated Node.js implant, performed host and AD reconnaissance, captured screenshots, and pivoted with WinRM. The chain can precede data theft, extortion, or ransomware.  
**Recommendations:** Restrict external Teams communication where business use does not require it; train users that IT support must not request unsolicited remote control; hunt for unusual RMM, PowerShell, Node.js, and WinRM sequences tied to external Teams contacts.  
**Source:** [Impersonating IT support: how threat actors turn a remote session into enterprise-wide access](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)

### Phishing that installs redundant RMM access
**Type:** Phishing, persistence, legitimate-tool abuse  
**Severity:** High  
**MITRE ATT&CK:** T1566.001, T1219, T1059.001, T1543.003, T1003  
**CVEs:** None reported  
**Affected:** Windows endpoints, MSP360 RMM, ConnectWise ScreenConnect, Microsoft Defender for Endpoint  
**M365/Azure relevance:** Meeting invitations, PDF lures, and update prompts can convert a user action into persistent administrative access that blends into normal IT activity.  
**Summary:** Microsoft observed phishing campaigns delivering a masqueraded MSP360 installer. After UAC elevation, the installer established MSP360 services and silently installed ScreenConnect, creating two remote-access paths. Operators then used the channels for credential access, local collection, and follow-on tooling.  
**Recommendations:** Maintain an approved RMM allowlist; alert on new RMM services and chained installation of multiple remote tools; use Defender hunting to identify uncommon RMM execution and PowerShell downloads.  
**Source:** [Phishing Abuses RMM Tools for Persistent Access](https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/)

### Star Blizzard RedFlick phishing and scheduled-task delivery
**Type:** State-sponsored phishing, malware delivery, persistence  
**Severity:** High  
**MITRE ATT&CK:** T1566.001, T1204.002, T1053.005, T1027, T1105  
**CVEs:** None reported  
**Affected:** Windows endpoints, email users, organizations supporting Ukraine and international policy work  
**M365/Azure relevance:** The campaign targets identities and users through large-scale phishing, then uses a low-friction delivery path designed to reduce detection and user interaction.  
**Summary:** Microsoft reports that Russian state actor Star Blizzard adopted RedFlick, a technique that uses scheduled tasks to deliver the CosmicPulse backdoor. Compromised websites, evolved phishing, and fewer required victim actions improve the actor’s reach and detection evasion.  
**Recommendations:** Apply Microsoft Defender detections and the published hunting queries; review new or anomalous scheduled tasks after phishing events; protect high-risk users connected to government, NGO, and Ukraine-related work with stronger conditional access and phishing-resistant MFA.  
**Source:** [Star Blizzard refines phishing and malware delivery with the RedFlick technique](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)

### Compromised Azure service principals used for destruction
**Type:** Cloud identity compromise, credential access, destructive operations  
**Severity:** Critical  
**MITRE ATT&CK:** T1078.004, T1526, T1087.004, T1552.001, T1485  
**CVEs:** None reported  
**Affected:** Azure Storage, SQL databases, Key Vault, Function Apps, VMs, App Services, recovery resources  
**M365/Azure relevance:** Workload identities can bypass user-focused controls and perform high-impact operations across subscriptions when permissions and secrets are poorly governed.  
**Summary:** Microsoft linked Azure reconnaissance, credential collection, and bulk resource destruction to Storm-3168, associated with JADEPUFFER. Two compromised service principals enumerated resources and destroyed or altered storage, databases, Key Vaults, VMs, App Services, and recovery protections.  
**Recommendations:** Inventory and rotate service-principal secrets; replace broad credentials with managed identities and workload-identity federation; enforce least privilege and protect recovery resources with separate administrative paths and monitoring.  
**Source:** [Storm-3168: Agentic-driven cloud attacks using compromised service principals](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)

### Zimbra exploitation and mailbox theft
**Type:** Exploitation of public-facing application, web shell, credential and email theft  
**Severity:** Critical  
**MITRE ATT&CK:** T1190, T1059.004, T1505.003, T1005, T1552.001  
**CVEs:** CVE-2026-73570  
**Affected:** Internet-facing Zimbra Collaboration Suite servers with the vulnerable SNMP notification path  
**M365/Azure relevance:** Compromised mail infrastructure can expose credentials, archives, and authentication material used against Microsoft 365 identities and business email workflows.  
**Summary:** Microsoft observed exploitation of an unauthenticated command-injection flaw in Zimbra. Attackers deployed web shells and reverse shells, escalated privileges, installed persistent access tools, accessed email, and collected authentication and mailbox data. Zimbra 10.1.20 contains the remediation.  
**Recommendations:** Patch to a remediated Zimbra version or remove the vulnerable component; investigate web shells, reverse shells, and mailbox archives; rotate credentials and tokens that were present on affected servers.  
**Source:** [Unauthenticated command injection on internet-facing mail servers: tracking CVE-2026-73570](https://www.microsoft.com/en-us/security/blog/2026/09/30/unauthenticated-command-injection-on-internet-facing-mail-servers-tracking-cve-2026-73570/), [Attackers have been exploiting critical Zimbra flaw to steal emails](https://arstechnica.com/security/2026/09/attackers-have-been-exploiting-critical-zimbra-flaw-to-steal-emails/)

### AI-assisted executive impersonation and invoice fraud
**Type:** Business email compromise, executive impersonation, payment fraud  
**Severity:** High  
**MITRE ATT&CK:** T1566.002, T1583.001, T1656, T1534  
**CVEs:** None reported  
**Affected:** Finance teams, email security controls, accounts-payable workflows  
**M365/Azure relevance:** The campaign used more than one million emails, trusted third-party delivery infrastructure, impersonation domains, fabricated CEO threads, and invoices to target enterprise payment processes.  
**Summary:** Microsoft observed AI-assisted templates impersonating CEOs and ServiceNow, with requests for ACH payments of nearly $50,000. The attack depends on business context and trusted communication patterns rather than endpoint malware.  
**Recommendations:** Require out-of-band verification for payment changes and urgent executive requests; enforce anti-impersonation and external-domain controls in Defender for Office 365; monitor look-alike domains and unusual third-party sender infrastructure.  
**Source:** [Protecting organizations from AI-assisted executive impersonation and invoice fraud](https://www.microsoft.com/en-us/security/blog/2026/09/10/protecting-organizations-ai-assisted-executive-impersonation-invoice-fraud/)

### ASCII smuggling in phishing mail
**Type:** Filter evasion, phishing  
**Severity:** Medium  
**MITRE ATT&CK:** T1027, T1566.002  
**CVEs:** None reported  
**Affected:** Exchange Online, Defender for Office 365, email users and filtering pipelines  
**M365/Azure relevance:** Invisible Unicode tag characters can split or hide lure words before email filters parse them, creating a detection gap across user, transport, and AI-assisted analysis layers.  
**Summary:** Microsoft observed high-volume phishing using invisible Unicode characters to obfuscate financial lure terms. Defender for Office 365 telemetry showed that layered protections blocked most messages, but Microsoft also published a hunting signature for the technique.  
**Recommendations:** Deploy Microsoft’s hunting signature; inspect normalized Unicode in mail analysis; combine content, sender, authentication, and URL signals instead of relying on keyword matching.  
**Source:** [ASCII smuggling crosses over from AI prompt injection to phishing evasion](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/)

## Threat Actor Activity

Star Blizzard, a Russian state actor, is using RedFlick, compromised websites, and lower-friction phishing to deliver CosmicPulse. Storm-3168, linked by Microsoft to JADEPUFFER, used compromised Azure service principals for reconnaissance, credential collection, and destructive cloud operations. EvilTokens operated as a phishing-as-a-service platform for device-code token theft. The Teams helpdesk campaign and the RMM campaign were described as human-operated or financially motivated activity; Microsoft did not assign a named actor to either.

## Recommended Actions

1. Enforce phishing-resistant MFA for privileged users and high-value roles, and alert on new authentication methods, impossible travel, device-code use, and anomalous Microsoft Graph, SharePoint, OneDrive, or Exchange collection.
2. Restrict Teams external collaboration and require a verified support process before users grant remote control. Maintain an approved RMM inventory and alert on unapproved MSP360, ScreenConnect, PowerShell, Node.js, or WinRM chains.
3. Inventory Entra applications, service principals, secrets, delegated permissions, and workload identities. Rotate exposed credentials, remove unused privileges, and isolate recovery resources from ordinary cloud administration.
4. Patch internet-facing mail and collaboration systems quickly. For CVE-2026-73570, upgrade Zimbra to 10.1.20 or later and investigate web shells, reverse shells, mailbox archives, and credential exposure.
5. Apply Defender hunting guidance for RedFlick, ASCII smuggling, RMM abuse, and cloud identity compromise. Correlate identity, email, endpoint, Teams, and cloud audit signals in Defender XDR and Sentinel.
6. Add out-of-band verification for payment requests, executive impersonation, authentication changes, and urgent IT support. Treat trusted tools and familiar collaboration channels as attack surfaces, not evidence of legitimacy.

## Sources

- [Preparing governments for an era of interconnected cyber risk](https://blogs.microsoft.com/on-the-issues/2026/10/01/preparing-governments-for-an-era-of-interconnected-cyber-risk/)
- [Attackers have been exploiting critical Zimbra flaw to steal emails](https://arstechnica.com/security/2026/09/attackers-have-been-exploiting-critical-zimbra-flaw-to-steal-emails/)
- [Unauthenticated command injection on internet-facing mail servers: tracking CVE-2026-73570](https://www.microsoft.com/en-us/security/blog/2026/09/30/unauthenticated-command-injection-on-internet-facing-mail-servers-tracking-cve-2026-73570/)
- [Phishing Abuses RMM Tools for Persistent Access](https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/)
- [Star Blizzard refines phishing and malware delivery with the RedFlick technique](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)
- [Storm-3168: Agentic-driven cloud attacks using compromised service principals](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)
- [Beyond the ransomware: Tracking Storm-2570’s consistent tradecraft across deployments](https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/)
- [Microsoft disrupts AI-assisted platform that compromised 12,000](https://arstechnica.com/security/2026/09/microsoft-disrupts-ai-assisted-platform-that-compromised-12000/)
- [Unmasking EvilTokens: Getting to the root of device code phishing](https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/)
- [Insights from the 2026 Microsoft Digital Defense Report](https://www.microsoft.com/en-us/security/blog/2026/10/01/insights-from-the-2026-microsoft-digital-defense-report/)
- [Protecting organizations from AI-assisted executive impersonation and invoice fraud](https://www.microsoft.com/en-us/security/blog/2026/09/10/protecting-organizations-ai-assisted-executive-impersonation-invoice-fraud/)
- [Threat matrix: Mapping threats across cloud web applications](https://www.microsoft.com/en-us/security/blog/2026/09/09/threat-matrix-mapping-threats-across-cloud-web-applications/)
- [Passkey-themed social engineering leads to identity and cloud compromise](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/)
- [ASCII smuggling crosses over from AI prompt injection to phishing evasion](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/)
- [Impersonating IT support: how threat actors turn a remote session into enterprise-wide access](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)
- [Counterfeit installers to system compromise: Tracking a deceptive software download campaign](https://www.microsoft.com/en-us/security/blog/2026/09/01/counterfeit-installers-system-compromise-tracking-deceptive-software-download-campaign/)
