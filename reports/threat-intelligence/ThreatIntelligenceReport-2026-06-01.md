# Threat Intelligence Report — 2026-06-01

## Executive Summary
This period is dominated by software supply-chain campaigns designed to steal CI/CD and cloud credentials, creating clean paths into Azure tenants and Microsoft 365 through stolen secrets and long-lived tokens. A second theme is identity-centric intrusion chains that begin at exposed edge or SaaS infrastructure and pivot into directory compromise. The most critical risk is uncontrolled credential exposure in developer and automation environments feeding direct access to cloud control planes.

## Key Threats

### Mini Shai-Hulud: Compromised npm packages stealing CI/CD secrets
**Type:** Supply chain / credential theft  
**Severity:** High  
**MITRE ATT&CK:** T1195.001, T1552.001, T1059  
**CVEs:** —  
**Affected:** npm dependencies; CI/CD runners (Linux GitHub Actions environments called out)  
**M365/Azure relevance:** Stolen CI/CD tokens and secrets routinely include Azure credentials (service principals, OIDC tokens, deployment secrets), enabling Azure subscription takeover and downstream access to Microsoft 365 via Entra-integrated apps.  
**Summary:** Malicious updates to popular npm packages executed during install to harvest automation secrets and exfiltrate credentials from build environments, expanding impact through dependency chains.  
**Recommendations:** Rotate CI/CD secrets and Entra app credentials; enforce least-privileged CI/CD identities; add package allowlists/lockfiles and block install-time scripts where feasible.  
**Source:** Mini Shai Hulud: Compromised @antv npm packages enable CI/CD credential theft — https://www.microsoft.com/en-us/security/blog/2026/05/20/mini-shai-hulud-compromised-antv-npm-packages-enable-ci-cd-credential-theft/

### Typosquatted npm packages targeting cloud and CI/CD credentials
**Type:** Supply chain / credential theft  
**Severity:** High  
**MITRE ATT&CK:** T1195.001, T1552.001, T1071.001  
**CVEs:** —  
**Affected:** npm ecosystem; developer workstations; automation environments  
**M365/Azure relevance:** Credential harvesting in build and developer contexts often yields Azure keys, GitHub tokens, and secrets used to deploy into Azure and access Entra-protected resources.  
**Summary:** Malicious typosquatted packages executed via npm lifecycle hooks and focused on stealing cloud and pipeline secrets, enabling follow-on compromise through stolen publish tokens and cloud credentials.  
**Recommendations:** Block outbound access from CI runners except to required endpoints; monitor for anomalous credential reads in build jobs; require short-lived, workload-identity-based auth for Azure deployments.  
**Source:** Typosquatted npm packages used to steal cloud and CI/CD secrets — https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/

### Dependency confusion against scoped npm namespaces for environment reconnaissance
**Type:** Supply chain / reconnaissance staging  
**Severity:** Medium  
**MITRE ATT&CK:** T1195.001, T1082, T1083  
**CVEs:** —  
**Affected:** npm installs using private/internal scopes; developer and build environments  
**M365/Azure relevance:** Reconnaissance of build environments can identify Azure/Entra secrets and internal endpoints (e.g., GitHub Enterprise/Azure DevOps), enabling targeted follow-on access and BEC-adjacent pivoting via identity.  
**Summary:** Malicious scoped packages impersonated internal namespaces to execute an obfuscated postinstall payload, collecting host and environment metadata with the design pattern of “recon now, exploit later.”  
**Recommendations:** Configure registries to prevent dependency confusion (scope pinning, private registry priority); inventory internal package scopes; alert on unexpected installs of private-scope packages from public registries.  
**Source:** Malicious npm packages abuse dependency confusion to profile developer environments — https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/

### Fox Tempest: Malware-signing-as-a-service abusing Microsoft Artifact Signing
**Type:** Trust abuse / malware distribution enablement  
**Severity:** High  
**MITRE ATT&CK:** T1553.002, T1583.006, T1588.002  
**CVEs:** —  
**Affected:** Windows endpoints; code-signing trust chains; Azure tenants/subscriptions created for abuse  
**M365/Azure relevance:** Signed malware increases success rates for phishing-to-endpoint compromise that often leads to token theft, MFA fatigue, and lateral movement into Entra/M365 administrative surfaces; Azure tenant creation at scale is also an abuse signal for identity defenders.  
**Summary:** A financially motivated operation generated short-lived fraudulent code-signing certificates and used Microsoft infrastructure at scale to help other criminal groups distribute malware and ransomware more effectively.  
**Recommendations:** Ensure Microsoft Defender tamper protection and cloud-delivered protection are enabled; hunt for suspicious signed binaries and abnormal certificate chains; harden Entra against credential replay with phishing-resistant MFA and token protections where available.  
**Source:** Exposing Fox Tempest: A malware-signing service operation — https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/

### Edge-to-internal intrusion chain via F5 BIG-IP and Confluence with identity compromise
**Type:** Initial access → credential theft → relay/AiTM identity attacks  
**Severity:** High  
**MITRE ATT&CK:** T1190, T1557, T1558, T1021  
**CVEs:** CVE-2025-53521  
**Affected:** F5 BIG-IP APM; internal Confluence; Active Directory authentication flows  
**M365/Azure relevance:** On-prem AD compromise commonly becomes an Entra compromise via synchronization paths, federated identity, or credential reuse; relay/AiTM tradecraft also mirrors Microsoft 365 targeting patterns.  
**Summary:** An intrusion started from an exposed edge appliance, pivoted to an internal server and SaaS app, then leveraged stolen credentials for relay-style authentication attacks against Active Directory.  
**Recommendations:** Patch and monitor edge appliances as tier-0 assets; isolate management planes; harden AD against relay (EPA, LDAP signing/channel binding where applicable) and reduce credential exposure; monitor for anomalous authentication and service ticket behavior.  
**Source:** From edge appliance to enterprise compromise: Multi-stage Linux intrusion via F5 and Confluence — https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/

### BadHost (CVE-2026-48710) in Starlette/FastAPI enabling auth bypass in agent and MCP-adjacent services
**Type:** Vulnerability / authentication bypass  
**Severity:** High  
**MITRE ATT&CK:** T1190, T1556, T1552.007  
**CVEs:** CVE-2026-48710  
**Affected:** Starlette (< 1.0.1); FastAPI and dependent services; exposed MCP/agent infrastructure  
**M365/Azure relevance:** Agent/MCP services frequently store Microsoft 365 Graph tokens or OAuth credentials for mailbox and SaaS access; an auth bypass can become direct mailbox access, message sending, or data exfiltration that looks like BEC.  
**Summary:** A Host-header-related path authorization bypass in Starlette was reported as broadly impacting FastAPI and related ecosystems, with particular risk for exposed agent/MCP services that aggregate credentials to external systems.  
**Recommendations:** Patch Starlette to fixed versions; restrict ingress to agent/MCP services (allowlists, mTLS/VPN); rotate stored Microsoft 365 OAuth credentials and enforce least-privileged app permissions.  
**Source:** Millions of AI agents imperiled by critical vulnerability in open source package — https://arstechnica.com/information-technology/2026/05/millions-of-ai-agents-imperiled-by-critical-vulnerability-in-open-source-package/

### SEO poisoning delivering ScreenConnect-based persistence and follow-on compromise
**Type:** Phishing/social engineering / remote access / ransomware precursor  
**Severity:** Medium  
**MITRE ATT&CK:** T1566.002, T1204, T1219, T1105  
**CVEs:** —  
**Affected:** End-user endpoints (Windows); ScreenConnect abused for persistence  
**M365/Azure relevance:** Endpoint footholds are a common bridge to Microsoft 365 (token theft, mailbox rule abuse, BEC enablement) and to Azure (credential discovery, lateral movement into admin tooling).  
**Summary:** A campaign used poisoned search results and lookalike download sites to deliver payloads and establish remote access via ScreenConnect, with tradecraft consistent with later-stage data theft or ransomware activity.  
**Recommendations:** Block known RMM tooling where not sanctioned; enforce ASR rules and SmartScreen; monitor for suspicious OAuth consent prompts and anomalous sign-ins following endpoint alerts.  
**Source:** From poisoned search results to GPU mining: A cryptojacking campaign abusing ScreenConnect and Microsoft .NET utilities — https://www.microsoft.com/en-us/security/blog/2026/05/26/poisoned-search-results-gpu-mining-cryptojacking-campaign-abusing-screenconnect-microsoft-net-utilities/

## Threat Actor Activity
- **Fox Tempest**: malware-signing-as-a-service enabling ransomware distribution.  
- **Secret Blizzard**: ongoing development and use of the Kazuar malware ecosystem.  
- **TeamPCP**: large-scale open-source supply chain poisoning, including GitHub-adjacent targeting.

## Recommended Actions
- Rotate and shorten-lived credentials: prioritize CI/CD secrets, Entra app credentials, PATs, and cloud keys; move to workload identity/OIDC where possible.
- Lock down software supply chain: pin dependencies, validate provenance/signatures where available, and block install-time scripts in high-risk build contexts.
- Treat edge appliances as tier-0: patch aggressively, restrict management access, and monitor for exploitation and anomalous authentication flows.
- Harden Microsoft 365 against identity-driven intrusion: phishing-resistant MFA for admins, Conditional Access with token/session controls, and strict OAuth app consent governance.
- Contain endpoint-to-cloud pivoting: enforce Defender protections, reduce local credential exposure, and alert on token theft indicators and anomalous Graph activity.

## Sources
- Malicious npm packages abuse dependency confusion to profile developer environments — https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/
- Typosquatted npm packages used to steal cloud and CI/CD secrets — https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/
- Mini Shai Hulud: Compromised @antv npm packages enable CI/CD credential theft — https://www.microsoft.com/en-us/security/blog/2026/05/20/mini-shai-hulud-compromised-antv-npm-packages-enable-ci-cd-credential-theft/
- Exposing Fox Tempest: A malware-signing service operation — https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/
- From edge appliance to enterprise compromise: Multi-stage Linux intrusion via F5 and Confluence — https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/
- Millions of AI agents imperiled by critical vulnerability in open source package — https://arstechnica.com/information-technology/2026/05/millions-of-ai-agents-imperiled-by-critical-vulnerability-in-open-source-package/
- From poisoned search results to GPU mining: A cryptojacking campaign abusing ScreenConnect and Microsoft .NET utilities — https://www.microsoft.com/en-us/security/blog/2026/05/26/poisoned-search-results-gpu-mining-cryptojacking-campaign-abusing-screenconnect-microsoft-net-utilities/

