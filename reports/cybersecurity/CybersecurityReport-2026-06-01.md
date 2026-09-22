# Cybersecurity Report — 2026-06-01

## Week in Security
This week was dominated by supply-chain abuse and identity-adjacent control failures. The sharpest signal was repeated abuse of developer ecosystems: malicious npm packages, poisoned open source dependencies, and threat actors using both search results and AI chatbot recommendations to steer victims to malware. Identity and tenant governance also stayed central, with passkey rollout lessons, shadow-tenant discovery, and new multitenant SOC controls all pointing to the same problem: security teams are still cleaning up sprawl while attackers move faster through trusted paths. One caveat sits outside the threat picture itself: the full `later` + `feed` Reader pool is heavily stale, especially in `feed`, so this report uses only the newest 2026 material and treats tag hygiene as an operational issue rather than pretending the broader collection is current.

## Notable Incidents & Breaches
The Dutch police and NCSC dismantled a botnet spanning more than 17 million devices and roughly 200 servers. The infrastructure was reportedly linked to the ASOCKS residential proxy network, which suggests a large dual-use ecosystem where infected consumer devices can be repurposed for fraud, phishing, and other criminal operations. The lesson is simple: unmanaged endpoints and consumer-grade apps still scale into national-level infrastructure risk.

A broader software supply-chain crisis kept expanding. TeamPCP was tied to a new wave of poisoned open source tooling that reportedly reached GitHub repositories and a growing list of downstream victims. The impact is not a single breach but a compounding trust failure: once developer tools are compromised, every build pipeline, package publish token, and dependent project becomes part of the blast radius.

Microsoft also detailed a multistage intrusion that started with a compromised F5 BIG-IP edge appliance, pivoted into an internal Linux server, then moved through a vulnerable Confluence instance toward Active Directory relay activity. The operational lesson is that internet-facing appliances, internal SaaS platforms, and identity infrastructure now form one attack path, even when defenders still monitor them as separate domains.

## Vulnerabilities & Patches
CVE-2026-48710, branded BadHost, stood out because it affects Starlette, a core Python framework used by FastAPI, vLLM, LiteLLM, MCP servers, and a wide range of AI tooling. The bug allows authentication bypass through a malformed `Host` header and creates obvious risk for exposed AI agent and MCP deployments that hold third-party credentials. Patch priority is high anywhere Starlette sits behind weak network controls or front-ends sensitive agent workflows.

The F5-to-Confluence intrusion chain is a reminder that unsupported or delayed edge appliance patching is still one of the fastest ways to hand attackers a foothold. Even where Windows systems are hardened, unpatched network appliances and internal web applications remain enough to bridge into identity compromise.

Developer ecosystems also saw active exploitation rather than hypothetical risk. Microsoft tracked one cluster of dependency-confusion packages impersonating internal enterprise namespaces and another typosquatting OpenSearch and related packages to steal AWS, Vault, npm, and GitHub Actions secrets. In both cases, install-time lifecycle hooks turned ordinary package installs into credential theft events.

## Threat Actor Activity
Multiple campaigns converged on the same tactic: abuse developer trust, then pivot into cloud and identity. One actor published dependency-confusion packages across fake corporate npm scopes, using `postinstall` hooks to fingerprint environments and prepare for follow-on exploitation. A second campaign used typosquatted npm packages to harvest AWS credentials, Vault tokens, npm publish tokens, and CI/CD secrets, with clear potential for downstream software supply-chain compromise.

Another campaign abused poisoned search results and, in some observed cases, AI chatbot software recommendations to distribute fake utilities that led to ScreenConnect-based persistence and GPU cryptomining. That combination matters because it joins old SEO poisoning tradecraft with new AI-mediated discovery paths, expanding the attack surface beyond browsers into assistant-driven user behavior.

TeamPCP’s continued poisoning of open source projects remains strategically important because the group is turning supply-chain compromise into a repeatable operating model rather than an occasional high-end intrusion. That changes the defensive problem from incident response to continuous dependency hygiene.

## Cloud & Identity Security
Passkeys remain one of the few clearly positive identity stories, but rollout discipline matters more than feature enablement. The strongest lesson from large-scale deployments is that passkeys fail when teams treat them as a toggle instead of a staged migration with telemetry, recovery design, and support planning.

Microsoft’s tenant governance push also reflects a real market problem: shadow tenants, old test tenants, and loosely governed multitenant relationships are becoming quiet exposure paths. Related-tenants discovery and quarantine workflows are useful because they turn hidden tenant sprawl into something operators can inventory and contain before an attacker does it for them.

On the SOC side, Microsoft Sentinel’s latest updates focused on multitenant administration, unified RBAC, and bringing AI-agent telemetry into the data lake. The larger point is not product expansion for its own sake. It is that SOC and MDR teams now need to monitor identities, tenants, and agents as first-class objects, not side data around endpoint alerts.

## Recommended Actions
1. Patch or isolate Starlette-based services, especially FastAPI, MCP, LiteLLM, and vLLM deployments exposed to untrusted traffic.
2. Audit npm, PyPI, and CI/CD dependency paths for lifecycle-hook abuse; enforce private-scope pinning, disable install scripts where possible, and rotate any cloud or publish tokens exposed to build systems.
3. Treat edge appliances and internal collaboration platforms as Tier-0 attack-path assets; enforce lifecycle replacement for unsupported F5 and similar devices, and patch internally exposed SaaS platforms with the same urgency as internet-facing systems.
4. Review identity recovery and tenant governance now: inventory related tenants, block or quarantine unknown tenants, and remove fallback authentication paths that weaken passkey or MFA posture.
5. Clean the Reader tag corpus feeding this report. The current `feed` and older `later` pool is stale enough to distort weekly reporting unless aggressively curated.

## Sources
- Introducing the updated exposure score in Microsoft Defender Vulnerability Management
  https://techcommunity.microsoft.com/t5/microsoft-defender-vulnerability/introducing-the-updated-exposure-score-in-microsoft-defender/ba-p/4524217
- 5 Lessons from Rolling Out Passkeys to Millions of Users
  https://entra.news/p/5-lessons-from-rolling-out-passkeys
- Malicious npm packages abuse dependency confusion to profile developer environments
  https://www.microsoft.com/en-us/security/blog/2026/05/29/33-malicious-npm-packages-abuse-dependency-confusion-profile-developer-environments/
- Typosquatted npm packages used to steal cloud and CI/CD secrets
  https://www.microsoft.com/en-us/security/blog/2026/05/28/typosquatted-npm-packages-used-steal-cloud-ci-cd-secrets/
- Botnet of more than 17 million devices dismantled
  https://arstechnica.com/security/2026/05/botnet-of-more-than-17-million-devices-dismantled/
- Websites have a new way to spy on visitors: analyzing their SSD activity
  https://arstechnica.com/security/2026/05/websites-have-a-new-way-to-spy-on-visitors-analyzing-their-ssd-activity/
- From poisoned search results to GPU mining: A cryptojacking campaign abusing ScreenConnect and Microsoft .NET utilities
  https://www.microsoft.com/en-us/security/blog/2026/05/26/poisoned-search-results-gpu-mining-cryptojacking-campaign-abusing-screenconnect-microsoft-net-utilities/
- Millions of AI agents imperiled by critical vulnerability in open source package
  https://arstechnica.com/information-technology/2026/05/millions-of-ai-agents-imperiled-by-critical-vulnerability-in-open-source-package/
- From edge appliance to enterprise compromise: Multi-stage Linux intrusion via F5 and Confluence
  https://www.microsoft.com/en-us/security/blog/2026/05/22/from-edge-appliance-to-enterprise-compromise-multi-stage-linux-intrusion-via-f5-and-confluence/
- A hacker group is poisoning open source code at an unprecedented scale
  https://arstechnica.com/information-technology/2026/05/a-hacker-group-is-poisoning-open-source-code-at-an-unprecedented-scale/
- Find shadow tenants and reduce risk fast with Microsoft Entra Tenant Governance
  https://techcommunity.microsoft.com/t5/microsoft-entra-blog/find-shadow-tenants-and-reduce-risk-fast-with-microsoft-entra/ba-p/4521996
- Organize your multitenant view with Tenant Groups in Microsoft Defender
  https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/organize-your-multitenant-view-with-tenant-groups-in-microsoft/ba-p/4522992
