# Threat Intelligence Report — 2026-09-14

## Executive Summary

September reporting is dominated by identity-led compromise and user-assisted execution. The most serious M365 risk is the passkey-themed campaign that establishes MFA persistence, abuses Microsoft Graph for reconnaissance, and reaches SharePoint, OneDrive, and email. ClickFix is now a broad delivery method across Windows and macOS, while AI-assisted executive impersonation is scaling invoice fraud against finance teams.

## Key Threats

### Passkey-themed social engineering and cloud compromise
**Type:** Identity phishing, MFA persistence, cloud data theft  
**Severity:** Critical  
**MITRE ATT&CK:** T1566.002, T1098.005, T1528, T1087.004, T1213  
**CVEs:** None reported  
**Affected:** Microsoft Entra ID, Microsoft Graph, SharePoint, OneDrive, Exchange Online  
**M365/Azure relevance:** Direct. Attackers use a passkey lure to obtain access, add persistence, enumerate the tenant through Graph, and collect cloud data.  
**Summary:** Microsoft reports a campaign in which social engineering themed around passkeys led to identity compromise and broader cloud access. The observed chain included MFA persistence, Graph reconnaissance, and access to SharePoint, OneDrive, and email.  
**Recommendations:** Review newly registered authentication methods and suspicious consent or session activity. Alert on unusual Graph enumeration and cross-service access. Require phishing-resistant authentication with tightly governed recovery paths.  
**Source:** [Passkey-themed social engineering leads to identity and cloud compromise](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/)

### Teams helpdesk impersonation
**Type:** Social engineering, remote access, lateral movement  
**Severity:** High  
**MITRE ATT&CK:** T1566.003, T1656, T1219, T1021, T1078  
**CVEs:** None reported  
**Affected:** Microsoft Teams external collaboration, user endpoints, enterprise identity  
**M365/Azure relevance:** Direct. The campaign abuses external Teams contact to impersonate IT support and move from a conversation into remote access and enterprise-wide activity.  
**Summary:** Microsoft observed a human-operated intrusion campaign that used Teams external collaboration to pose as IT support, obtain a remote session, deploy a Node.js implant, and move laterally with legitimate tools.  
**Recommendations:** Restrict external Teams communication where business use does not require it. Train service desk staff to reject unsolicited remote-support requests. Hunt for new remote tools, Node.js execution, and unusual Teams-to-endpoint activity.  
**Source:** [Impersonating IT support: how threat actors turn a remote session into enterprise-wide access](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)

### AI-assisted executive impersonation and invoice fraud
**Type:** Business email compromise, payment fraud  
**Severity:** High  
**MITRE ATT&CK:** T1583.001, T1585.002, T1566.002, T1036.002, T1656  
**CVEs:** None reported  
**Affected:** Exchange Online, finance and accounts-payable workflows, third-party mail infrastructure  
**M365/Azure relevance:** Direct. Microsoft observed more than one million messages, lookalike domains, spoofed executives, fabricated ServiceNow threads, and ACH payment requests.  
**Summary:** The campaign targeted finance staff with personalized CEO impersonation and fake invoices for payments of nearly $50,000. AI-assisted template construction improved consistency, but mismatched headers, display names, and thread formatting remained useful detection clues.  
**Recommendations:** Enforce payment verification through an out-of-band channel. Tune Defender for Office 365 for lookalike domains, display-name mismatch, and payment lures. Protect executive identities and finance workflows with phishing-resistant authentication and dual approval.  
**Source:** [Protecting organizations from AI-assisted executive impersonation and invoice fraud](https://www.microsoft.com/en-us/security/blog/2026/09/10/protecting-organizations-ai-assisted-executive-impersonation-invoice-fraud/)

### ClickFix and TerminalFix delivery chains
**Type:** User-assisted execution, malware delivery, reverse tunneling  
**Severity:** High  
**MITRE ATT&CK:** T1204.002, T1059.001, T1059.004, T1218, T1574.002, T1090.001  
**CVEs:** None reported  
**Affected:** Windows and macOS endpoints, browsers, PowerShell, Windows Run, macOS Terminal  
**M365/Azure relevance:** High. Compromised endpoints provide token, browser-session, and credential access into M365 tenants. The technique also bypasses the trust normally supplied by signed installers.  
**Summary:** ClickFix has become a mainstream lure. Fake CAPTCHA pages persuade users to paste commands into PowerShell, Windows Run, or Terminal. Microsoft’s TerminalFix reporting adds DLL sideloading and a reverse tunnel to the chain, while macOS campaigns hide lures behind browser-fingerprinting gates.  
**Recommendations:** Block suspicious script interpreters and unsigned child processes from browsers. Monitor clipboard-to-shell behavior, suspicious PowerShell, and reverse-tunnel tools. Use Defender for Endpoint attack-surface reduction and browser protections on both Windows and macOS.  
**Source:** [ClickFix attacks infecting PCs and Macs are going viral](https://arstechnica.com/security/2026/09/clickfix-attacks-infecting-pcs-and-macs-are-going-viral/), [TerminalFix campaign deploys a reverse tunnel through multistage intrusion](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/), [From open lures to cloaked gates: How a macOS ClickFix campaign learned to hide](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/)

### ASCII smuggling in phishing
**Type:** Defense evasion, phishing  
**Severity:** High  
**MITRE ATT&CK:** T1027, T1566.001  
**CVEs:** None reported  
**Affected:** Email clients, mail security gateways, Defender for Office 365  
**M365/Azure relevance:** Direct. Invisible Unicode characters can hide words from filters while remaining operationally meaningful to the recipient.  
**Summary:** Microsoft reports that ASCII smuggling has moved from AI prompt-injection research into phishing. Attackers use invisible Unicode characters to obfuscate terms before mail filters parse the message, reducing the value of simple keyword detections.  
**Recommendations:** Normalize Unicode before content inspection and hunting. Combine text analysis with sender, URL, authentication, and behavioral signals. Test mail-flow rules against confusable characters and rendered-versus-raw content.  
**Source:** [ASCII smuggling crosses over from AI prompt injection to phishing evasion](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/)

### Counterfeit installers and software impersonation
**Type:** Malware delivery, masquerading  
**Severity:** High  
**MITRE ATT&CK:** T1189, T1036.005, T1204.002, T1218  
**CVEs:** None reported  
**Affected:** Windows endpoints, software download workflows, Defender XDR  
**M365/Azure relevance:** High. A compromised endpoint can expose browser sessions, credentials, and M365 tokens.  
**Summary:** Microsoft observed look-alike download pages and regenerated installer archives impersonating legitimate vendors. The campaign included Defender XDR detections, hunting guidance, and indicators of compromise, showing that software acquisition remains a practical entry point.  
**Recommendations:** Allow software installation from managed sources only. Block newly registered look-alike domains and executable downloads from untrusted sites. Use application control and investigate installer launches from browser and temporary directories.  
**Source:** [Counterfeit installers to system compromise: Tracking a deceptive software download campaign](https://www.microsoft.com/en-us/security/blog/2026/09/01/counterfeit-installers-system-compromise-tracking-deceptive-software-download-campaign/)

### Supply-chain credential exposure
**Type:** Software supply-chain compromise, credential theft  
**Severity:** Critical  
**MITRE ATT&CK:** T1195.002, T1552.001, T1552.004, T1539  
**CVEs:** None reported  
**Affected:** LiteLLM and other developer packages, CI/CD pipelines, cloud credentials, GitHub/GitLab tokens  
**M365/Azure relevance:** High where exposed secrets grant access to Azure subscriptions, Microsoft 365 integrations, registries, or automation identities.  
**Summary:** Researchers reported that compromised LiteLLM versions exposed credentials from hundreds of thousands of CI/CD pipelines during a short attack window. Microsoft separately described ChainDrop, a self-propagating worm in more than 400 npm packages. The shared lesson is operational: package trust and secret lifetime determine blast radius.  
**Recommendations:** Identify affected package versions and rotate every secret accessible to them. Prefer short-lived workload identities over static keys. Add package provenance checks, dependency pinning, egress controls, and CI secret scanning.  
**Source:** [Terabytes of credentials leaked in massive supply-chain attack](https://arstechnica.com/security/2026/08/terabytes-of-credentials-leaked-in-massive-supply-chain-attack/), [ChainDrop supply chain compromise: Anatomy of a self-propagating worm](https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/)

### DeadLock ransomware
**Type:** Ransomware, double extortion  
**Severity:** High  
**MITRE ATT&CK:** T1486, T1490, T1562.001, T1657  
**CVEs:** None reported  
**Affected:** Windows and enterprise file services, victim communications and data-leak infrastructure  
**M365/Azure relevance:** High. Cloud identity, SaaS collaboration, and backup access are likely to be targeted during impact and extortion operations.  
**Summary:** Microsoft describes DeadLock as a financially motivated operation using a Rust-based encryptor and decentralized infrastructure for victim communications, negotiations, and data-leak operations. The operation combines encryption with pressure to prevent recovery and force payment.  
**Recommendations:** Isolate backup administration from ordinary tenant identities. Test recovery without relying on reachable production credentials. Monitor for mass file changes, backup tampering, and unusual access to sensitive SharePoint or OneDrive data.  
**Source:** [DeadLock ransomware: Breaking down a Rust-based encryptor with decentralized recovery infrastructure](https://www.microsoft.com/en-us/security/blog/2026/08/10/deadlock-ransomware-breaking-down-a-rust-based-encryptor-with-decentralized-recovery-infrastructure/)

## Threat Actor Activity

Microsoft attributes the Teams intrusion to a human-operated campaign but does not name a group in the cited article. TerminalFix and the macOS ClickFix reporting describe active campaigns without a definitive public actor attribution. TeamPCP is associated by researchers with the LiteLLM and related package compromises. Ars Technica also reports that Kremlin-backed groups are adopting ClickFix, while the supplied material does not establish a specific group for the September campaigns.

## Recommended Actions

1. Audit Entra authentication methods, refresh-token activity, risky sign-ins, OAuth grants, and Graph enumeration for the last 30 days.
2. Restrict Teams external access and require a verified internal process for remote support.
3. Add payment verification controls and mail detections for lookalike domains, executive display-name spoofing, Unicode obfuscation, and ACH lures.
4. Hunt for ClickFix indicators: browser-launched shells, clipboard-to-PowerShell or Terminal execution, DLL sideloading, and reverse tunnels.
5. Review endpoint application control and software installation paths, including macOS coverage.
6. Inventory dependencies and rotate secrets exposed to compromised packages. Replace long-lived CI/CD credentials with workload identity and short-lived tokens.
7. Confirm offline or logically isolated backups, recovery roles, and tenant-wide ransomware response procedures.

## Sources

- [ClickFix attacks infecting PCs and Macs are going viral](https://arstechnica.com/security/2026/09/clickfix-attacks-infecting-pcs-and-macs-are-going-viral/)
- [Protecting organizations from AI-assisted executive impersonation and invoice fraud](https://www.microsoft.com/en-us/security/blog/2026/09/10/protecting-organizations-ai-assisted-executive-impersonation-invoice-fraud/)
- [Threat matrix: Mapping threats across cloud web applications](https://www.microsoft.com/en-us/security/blog/2026/09/09/threat-matrix-mapping-threats-across-cloud-web-applications/)
- [4 groups caught using the same Chrome and Windows exploit kit](https://arstechnica.com/information-technology/2026/09/4-groups-caught-using-the-same-chrome-and-windows-exploit-kit/)
- [Passkey-themed social engineering leads to identity and cloud compromise](https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/)
- [ASCII smuggling crosses over from AI prompt injection to phishing evasion](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/)
- [Impersonating IT support: how threat actors turn a remote session into enterprise-wide access](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)
- [Counterfeit installers to system compromise: Tracking a deceptive software download campaign](https://www.microsoft.com/en-us/security/blog/2026/09/01/counterfeit-installers-system-compromise-tracking-deceptive-software-download-campaign/)
- [TerminalFix campaign deploys a reverse tunnel through multistage intrusion](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)
- [Authorities arrest 2 alleged members of prolific hacking group TeamPCP](https://arstechnica.com/security/2026/08/authorities-arrest-2-alleged-members-of-prolific-hacking-group-teampcp/)
- [Hunting MacSync Stealer infrastructure through behavioral pivots](https://www.microsoft.com/en-us/security/blog/2026/08/18/hunting-macsync-stealer-infrastructure-through-behavioral-pivots/)
- [DeadLock ransomware: Breaking down a Rust-based encryptor with decentralized recovery infrastructure](https://www.microsoft.com/en-us/security/blog/2026/08/10/deadlock-ransomware-breaking-down-a-rust-based-encryptor-with-decentralized-recovery-infrastructure/)
- [From open lures to cloaked gates: How a macOS ClickFix campaign learned to hide](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/)
- [ChainDrop supply chain compromise: Anatomy of a self-propagating worm](https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/)
- [Terabytes of credentials leaked in massive supply-chain attack](https://arstechnica.com/security/2026/08/terabytes-of-credentials-leaked-in-massive-supply-chain-attack/)
- [Thousands of servers can be backdoored by exploiting buggy motherboard controllers](https://arstechnica.com/security/2026/08/thousands-of-servers-can-be-backdoored-by-exploiting-buggy-motherboard-controllers/)
- [Vulnerability giving attackers full control of Macs is under active exploitation](https://arstechnica.com/security/2026/08/vulnerability-giving-attackers-full-control-of-macs-is-under-active-exploitation/)
- [BGP hijack infecting networks caused by a comedy of errors that’s not funny at all](https://arstechnica.com/security/2026/09/well-executed-bgp-attack-uses-hijacked-ips-to-infect-real-networks/)

