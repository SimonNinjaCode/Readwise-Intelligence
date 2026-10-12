# Threat Intelligence Report — 2026-10-12

## Executive Summary

The reporting window contained limited relevant material in October, so the window was extended exactly one month to September. The strongest signals are identity-led cloud compromise, device-code phishing, social engineering through Teams, and attackers abusing trusted remote-access tooling; Storm-3168 shows the destructive potential when compromised service principals reach Azure control planes.

## Key Threats

### Device-code phishing and token theft at scale
**Type:** Phishing-as-a-Service, OAuth/device-code abuse, business email compromise  
**Severity:** Critical  
**MITRE ATT&CK:** T1528, T1078.004, T1566  
**CVEs:** None  
**Affected:** Microsoft Entra ID, Microsoft 365, Exchange Online, user mailboxes  
**M365/Azure relevance:** EvilTokens compromised more than 12,000 inboxes across over 10,000 organizations by automating device-code phishing, token theft, inbox analysis, and follow-on BEC.  
**Summary:** EvilTokens turns a difficult identity attack into a repeatable service. Stolen tokens bypass password resets and can provide access to mail, files, and Graph-backed data until sessions and refresh tokens are revoked.  
**Recommendations:** Restrict device-code authentication where it is not required; enforce phishing-resistant authentication and risk-based Conditional Access; hunt for unusual device-code sign-ins, new authentication methods, and high-volume Graph activity.  
**Source:** [Unmasking EvilTokens: Getting to the root of device code phishing](https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/)

### Cloud identity compromise through social engineering
**Type:** Identity compromise, persistence, cloud data collection  
**Severity:** Critical  
**MITRE ATT&CK:** T1598.003, T1078.004, T1556.006, T1087.004  
**CVEs:** None  
**Affected:** Microsoft Entra ID, Microsoft Graph, SharePoint Online, OneDrive, Exchange Online  
**M365/Azure relevance:** Microsoft observed added authentication methods, unusual sign-ins, Graph enumeration, SharePoint and OneDrive downloads, and email collection through REST APIs. A separate Storm-3068 case shows how one compromised identity expanded into Azure DevOps, pipelines, Kubernetes, and connected cloud infrastructure.  
**Summary:** The attack path is identity-first: social engineering, persistence, reconnaissance, content discovery, and collection. Password resets alone are insufficient when attackers add authentication methods or retain valid tokens.  
**Recommendations:** Alert on attacker-added authentication methods and anomalous Graph/API volume; require step-up authentication for security-info changes; gate stolen-token use with compliant-network and device conditions.  
**Source:** [Passkey-themed social engineering leads to identity and cloud compromise](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/) and [Beyond source code: A path to the keys to the kingdom](https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/)

### Azure destruction through compromised service principals
**Type:** Cloud account compromise, resource destruction, credential access  
**Severity:** Critical  
**MITRE ATT&CK:** T1078.004, T1526, T1485, T1490  
**CVEs:** None  
**Affected:** Azure Storage, SQL databases, Key Vault, Function Apps, virtual machines, App Services, recovery controls  
**M365/Azure relevance:** Storm-3168 used compromised service principals for Azure reconnaissance, credential collection, and bulk destructive operations.  
**Summary:** Service principals are machine identities with broad reach and weak interactive-login visibility. Once compromised, they can delete data and recovery protections at a speed that outpaces manual response.  
**Recommendations:** Apply least privilege and workload-identity governance; monitor service-principal sign-ins and destructive Azure Activity operations; separate recovery administration and protect it with privileged access workflows.  
**Source:** [Storm-3168: Agentic-driven cloud attacks using compromised service principals](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)

### Teams helpdesk impersonation and remote-access persistence
**Type:** Social engineering, remote-access abuse, hands-on-keyboard intrusion  
**Severity:** High  
**MITRE ATT&CK:** T1566.003, T1218.007, T1218.011, T1059.001, T1087.002  
**CVEs:** None  
**Affected:** Microsoft Teams external collaboration, Windows endpoints, Active Directory, RMM platforms  
**M365/Azure relevance:** Attackers used Teams to impersonate IT support, persuaded users to grant interactive remote sessions, then deployed PowerShell, MSI, Node.js, and a persistent JavaScript implant. A related campaign abused MSP360 to install ScreenConnect as a second access path.  
**Summary:** Trusted collaboration and remote-management tools become the attack chain. The absence of an exploit does not reduce the impact: the attacker receives a user-approved foothold and performs reconnaissance across the enterprise.  
**Recommendations:** Restrict external Teams communication and verify helpdesk identities out of band; require approval and logging for remote-support tools; alert on new RMM installations, portable runtimes, and suspicious PowerShell from support sessions.  
**Source:** [Impersonating IT support: how threat actors turn a remote session into enterprise-wide access](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/) and [Phishing Abuses RMM Tools for Persistent Access](https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/)

### Star Blizzard’s RedFlick delivery and targeted phishing
**Type:** State-sponsored phishing, malware delivery, detection evasion  
**Severity:** High  
**MITRE ATT&CK:** T1566, T1204, T1027  
**CVEs:** None  
**Affected:** Microsoft 365 users, NGOs, governments, think tanks, Ukrainian-linked organizations  
**M365/Azure relevance:** Star Blizzard used compromised websites, large-scale phishing, and RedFlick delivery to evade detection and support cyberespionage. Microsoft provides Defender detections, hunting queries, and indicators.  
**Summary:** The campaign targets trust relationships and detection blind spots rather than a single software flaw. Its focus on policy, government, and Ukraine-related organizations makes it relevant to customers with geopolitical exposure.  
**Recommendations:** Deploy the supplied Defender detections and hunting queries; harden Safe Links and attachment policies; review sign-ins and mailbox activity after phishing events.  
**Source:** [Star Blizzard refines phishing and malware delivery with the RedFlick technique](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)

### Zimbra command injection and email theft
**Type:** Unauthenticated remote command injection, web-shell persistence, data theft  
**Severity:** Critical  
**MITRE ATT&CK:** T1190, T1059.004, T1105, T1505.003  
**CVEs:** CVE-2026-73570  
**Affected:** Internet-facing Zimbra Collaboration Suite servers with the SNMP package and notifications enabled  
**M365/Azure relevance:** Compromised mail infrastructure can expose credentials, archives, and authentication material used against Microsoft 365 or hybrid identity environments.  
**Summary:** A crafted email can trigger unauthenticated OS command execution. Microsoft observed web shells, reverse shells, persistence, mailbox access, archive creation, and transfer activity.  
**Recommendations:** Patch or isolate exposed Zimbra servers; disable the vulnerable optional component where possible; hunt for web shells, unexpected JSP files, reverse shells, and mailbox archive access.  
**Source:** [Unauthenticated command injection on internet-facing mail servers: tracking CVE-2026-73570](https://www.microsoft.com/en-us/security/blog/2026/09/30/unauthenticated-command-injection-on-internet-facing-mail-servers-tracking-cve-2026-73570/) and [Attackers have been exploiting critical Zimbra flaw to steal emails](https://arstechnica.com/security/2026/09/attackers-have-been-exploiting-critical-zimbra-flaw-to-steal-emails/)

### AI-themed phishing, executive impersonation, and ClickFix
**Type:** Phishing, BEC, malvertising, user-executed command abuse  
**Severity:** High  
**MITRE ATT&CK:** T1566.001, T1566.003, T1036, T1656, T1657  
**CVEs:** None  
**Affected:** Microsoft 365 mailboxes, Windows and macOS endpoints, finance and executive workflows  
**M365/Azure relevance:** Microsoft observed AI-themed campaigns using ChatGPT, Copilot, DeepSeek, and Claude branding, including a campaign sending up to 100,000 emails per day. Separate campaigns used AI-assisted executive impersonation, invoice fraud, invisible Unicode characters, and ClickFix terminal commands.  
**Summary:** Attackers are borrowing trusted brands and normal business processes. ASCII smuggling can defeat naive email parsing, while ClickFix converts a user interaction into direct command execution on both PCs and Macs.  
**Recommendations:** Block or detonate suspicious AI-themed links and attachments; add Unicode/ASCII-smuggling detections; train users and finance teams to verify payment and support requests through an independent channel.  
**Source:** [Detect and disrupt AI-themed attacks with Microsoft Defender](https://www.microsoft.com/en-us/security/blog/2026/09/10/detect-and-disrupt-ai-themed-attacks-with-microsoft-defender/), [Protecting organizations from AI-assisted executive impersonation and invoice fraud](https://www.microsoft.com/en-us/security/blog/2026/09/10/protecting-organizations-ai-assisted-executive-impersonation-invoice-fraud/), [ASCII smuggling crosses over from AI prompt injection to phishing evasion](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/), and [ClickFix attacks infecting PCs and Macs are going viral](https://arstechnica.com/security/2026/09/clickfix-attacks-infecting-pcs-and-macs-are-going-viral/)

## Threat Actor Activity

Named activity in the selected material includes EvilTokens operators, Storm-3068, Storm-3168/JADEPUFFER, Storm-2570, Star Blizzard, and the operators behind NeedyMantis. Microsoft also describes broader AI-assisted phishing and BEC activity without assigning it to a single actor. NeedyMantis is a post-compromise malware family used in targeted operations against telecommunications, universities, medical nonprofits, intergovernmental organizations, and government contractors.

## Recommended Actions

1. Review Entra sign-in logs for device-code authentication, unfamiliar authentication methods, anomalous Graph volume, impossible travel, and access from new infrastructure.
2. Enforce phishing-resistant authentication, restrict device-code flow, and use compliant-network or device conditions to reduce the value of stolen refresh tokens.
3. Audit service principals, managed identities, Azure roles, and recent destructive operations; separate recovery administration from ordinary cloud operations.
4. Restrict external Teams collaboration and formalize helpdesk identity verification before remote support.
5. Deploy Microsoft’s supplied Defender detections and hunting queries for EvilTokens, Star Blizzard, Storm-2570, RedFlick, ASCII smuggling, and Teams/helpdesk campaigns.
6. Patch or isolate internet-facing Zimbra systems and review hybrid identity paths for stolen credentials or mailbox data.
7. Add payment-change and executive-request verification controls that do not rely on email or Teams alone.

## Sources

- [Stolen Tokens, Agents and Universal CAE: What Global Secure Access Adds to Entra ID](https://entra.news/p/stolen-tokens-agents-and-universal)
- [Unauthenticated command injection on internet-facing mail servers: tracking CVE-2026-73570](https://www.microsoft.com/en-us/security/blog/2026/09/30/unauthenticated-command-injection-on-internet-facing-mail-servers-tracking-cve-2026-73570/)
- [Attackers have been exploiting critical Zimbra flaw to steal emails](https://arstechnica.com/security/2026/09/attackers-have-been-exploiting-critical-zimbra-flaw-to-steal-emails/)
- [Phishing Abuses RMM Tools for Persistent Access](https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/)
- [Beyond source code: A path to the keys to the kingdom](https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/)
- [Star Blizzard refines phishing and malware delivery with the RedFlick technique](https://www.microsoft.com/en-us/security/blog/2026/09/29/star-blizzard-refines-phishing-and-malware-delivery-with-the-redflick-technique/)
- [NeedyMantis: Unpacking a post-compromise malware family used in targeted operations](https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/)
- [Storm-3168: Agentic-driven cloud attacks using compromised service principals](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)
- [Beyond the ransomware: Tracking Storm-2570’s consistent tradecraft across deployments](https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/)
- [Unmasking EvilTokens: Getting to the root of device code phishing](https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/)
- [Microsoft disrupts AI-assisted platform that compromised 12,000](https://arstechnica.com/security/2026/09/microsoft-disrupts-ai-assisted-platform-that-compromised-12000/)
- [Muse, Meta's extraordinarily privileged AI assistant, has a serious 0-day](https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/)
- [How to track browser extension installations with Microsoft Defender](https://jeffreyappel.nl/how-to-track-browser-extension-installations-with-microsoft-defender/)
- [ClickFix attacks infecting PCs and Macs are going viral](https://arstechnica.com/security/2026/09/clickfix-attacks-infecting-pcs-and-macs-are-going-viral/)
- [Protecting organizations from AI-assisted executive impersonation and invoice fraud](https://www.microsoft.com/en-us/security/blog/2026/09/10/protecting-organizations-ai-assisted-executive-impersonation-invoice-fraud/)
- [Detect and disrupt AI-themed attacks with Microsoft Defender](https://www.microsoft.com/en-us/security/blog/2026/09/10/detect-and-disrupt-ai-themed-attacks-with-microsoft-defender/)
- [Threat matrix: Mapping threats across cloud web applications](https://www.microsoft.com/en-us/security/blog/2026/09/09/threat-matrix-mapping-threats-across-cloud-web-applications/)
- [Passkey-themed social engineering leads to identity and cloud compromise](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/)
- [ASCII smuggling crosses over from AI prompt injection to phishing evasion](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/)
- [Impersonating IT support: how threat actors turn a remote session into enterprise-wide access](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)

