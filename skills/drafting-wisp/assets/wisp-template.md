# Written Information Security Plan (WISP)

**{{FIRM_NAME}}**
Effective date: {{EFFECTIVE_DATE}}. Next annual review: {{REVIEW_DATE}}

> DRAFT for review by the firm's owner and Data Security Coordinator. This plan follows the structure of the sample in IRS Publication 5708 (Rev. 8-2024). It has not been reviewed by a lawyer or security professional and is not complete until every bracketed item is resolved and the plan is signed.

## I. Objective

The objective of this Written Information Security Plan is to create effective administrative, technical and physical safeguards for the personally identifiable information (PII) retained by {{FIRM_NAME}} (the Firm), and to comply with the Firm's obligations under the Gramm-Leach-Bliley Act and the Federal Trade Commission Safeguards Rule.

For this plan, PII means a first name or initial and last name of a client, spouse, dependent or employee in combination with any of the following retained by the Firm:

- Social Security number, date of birth or employment data
- Driver's license or state identification number
- Income, tax filing, retirement plan, asset ownership or investment data
- Financial account, credit card or debit card number, with or without any code or password that permits access to the account
- Email address, unlisted phone number, or residential or mobile contact information

PII does not include information lawfully available to the general public.

## II. Purpose

This plan is intended to:

- Ensure the security and confidentiality of all PII the Firm retains
- Protect PII against anticipated threats or hazards to its security or integrity
- Protect against unauthorized access to or use of PII that creates a substantial risk of identity theft or fraud

## III. Scope

Under this plan the Firm will:

- Identify reasonably foreseeable internal and external risks to records containing PII, whether electronic or paper
- Assess the likelihood and potential damage of those risks, considering the sensitivity of the PII
- Evaluate whether existing policies, systems and safeguards control those risks
- Design and implement safeguards to minimize those risks
- Regularly monitor and test the safeguards

## IV. Responsible officials

**Data Security Coordinator (DSC):** {{DSC_NAME}}, {{DSC_TITLE}}. The DSC serves as the Firm's Qualified Individual under the Safeguards Rule and will:

- Implement this plan and its daily operating procedures
- Identify every place the Firm stores PII and restrict access to it
- Confirm that everyone with access to PII completes security training at least annually and signs the acknowledgement in Attachment D
- Monitor and test compliance with this plan
- Evaluate third-party service providers' ability to protect PII, and require them by contract to do so
- Review this plan at least annually and whenever the Firm's business or systems change materially

**Public Information Officer (PIO):** {{PIO_NAME}}. The PIO approves all outward-facing communication about a security incident, including statements to clients, law enforcement, the media and business associates.

## V. Risk assessment

**Information the Firm handles:** {{PII_TYPES}}

**Where data could be lost:**

| Risk | Internal or external | Current safeguard | Gap or action |
|---|---|---|---|
{{RISK_ROWS}}

**Monitoring and testing:** {{MONITORING_PROCEDURE}}

## VI. Risk mitigation inside the Firm

### PII collection and retention

- The Firm collects only the PII needed for legitimate business purposes.
- Access to records containing PII is limited to people whose duties require it.
- PII is stored only in the locations listed in Attachment E and in these systems: {{SYSTEMS_WITH_PII}}
- Records containing PII are destroyed or deleted at the earliest opportunity consistent with business needs and legal retention requirements, as set out in Attachment A.

### Personnel accountability

- Every employee and contractor receives this plan when they start and signs Attachment D.
- New personnel are trained before they are given access to PII. {{BACKGROUND_CHECK_POLICY}}
- Paper records containing PII are locked away when not in use. Computers are locked when unattended.
- On termination, logins, remote access, email and physical access are disabled the same day, and keys and devices are returned.
- Wilful disclosure of PII or failure to follow this plan leads to disciplinary action up to termination.

### PII disclosure

- No PII is disclosed without authenticating the recipient and holding the client's written authorization.
- Visitors are escorted in any area where PII is stored.
- Records taken offsite are the minimum necessary, are never left unattended, and are returned promptly.
- The Firm shares client PII in the normal course of business with: {{THIRD_PARTIES}}. Each service provider with access to PII must maintain safeguards at least equal to this plan.

### Reportable events

- Any suspected loss or theft of PII is reported to the DSC immediately.
- The DSC follows the procedures in Attachment C, conducts a post-incident review, and records any resulting changes as an addendum to this plan.
- Insurance and counsel: {{CYBER_INSURANCE_AND_COUNSEL}}

## VII. Risk mitigation outside the Firm

### Network protection

- Firewall, operating system patches and security software are kept current on every device that accesses, stores or processes PII. {{PATCHING_DETAIL}}
- Anti-virus and anti-malware software: {{ANTIVIRUS_PRODUCT}}
- Event logging stays enabled on systems containing PII, and logs are reviewed at intervals of no more than 90 days.
- The DSC conducts a security review at least every 30 days.
- Backups: {{BACKUP_PROCEDURE}}

### User access control

- Multi-factor authentication is required for every person accessing any system that holds PII: {{MFA_DETAIL}}
- Every user has a unique login. There are no shared accounts or passwords.
- Passwords follow current NIST guidance, are at least 12 characters, are never reused across sites, and are changed when there is evidence of compromise. Password manager: {{PASSWORD_MANAGER}}

### Electronic exchange of PII

- PII is never sent in unprotected email. Clients exchange documents with the Firm through: {{SECURE_EXCHANGE_METHOD}}
- If a password-protected file must be sent, the password travels by a different channel than the file.
- Removable drives holding PII are encrypted.

### Wi-Fi

- Firm Wi-Fi uses strong encryption and a password. Guest Wi-Fi, if offered, is a separate network.
- Default passwords are changed on every wireless-capable device, including printers and smart devices.

### Remote access

- Remote access is approved by the DSC, encrypted, and allowed only with multi-factor authentication. {{REMOTE_ACCESS_DETAIL}}

### Connected devices

- New devices are reviewed for patches and password settings before they join the network.
- AutoRun is disabled for USB ports and optical drives.
- Drives and storage devices are securely erased or physically destroyed at the end of their service life.

### Information security training

- The DSC trains all personnel on paper and electronic record handling and on this plan at least annually. New personnel are trained before PII access is granted.

## VIII. Implementation

Effective {{EFFECTIVE_DATE}}, {{FIRM_NAME}} has adopted this Written Information Security Plan to comply with the Gramm-Leach-Bliley Act and the Federal Trade Commission Safeguards Rule.

Signed: ______________________ Date: __________
{{OWNER_NAME}}, {{OWNER_TITLE}}

Signed: ______________________ Date: __________
{{DSC_NAME}}, Data Security Coordinator

---

## Attachment A: Record retention policy

The Firm retains no PII longer than current regulations, practices or standards require.

- No paper or electronic record containing PII is kept longer than {{RETENTION_YEARS}} years, unless a specific legal requirement applies.
- Paper records are destroyed by cross-cut shredding or incineration at the end of their service life.
- Electronic records are destroyed by secure deletion and overwriting, or by reformatting or destroying the drive.

## Attachment B: Rules of behavior for safeguarding client PII

Everyone who uses the Firm's systems agrees to:

- Not open unexpected email attachments or links; verify with the sender by phone first
- Keep business and personal computers, phones and email accounts separate
- Not connect personal or unknown storage devices to Firm computers or networks
- Download software only with the DSC's approval
- Never give out usernames, passwords or details of the Firm's systems, and report any attempt to obtain them
- Use strong, unique passwords and multi-factor authentication
- Conduct online business only over a secure connection

## Attachment C: Security breach procedures and notifications

If the DSC determines that PII has been stolen or lost, the Firm will notify, as applicable:

- The IRS Stakeholder Liaison for the Firm's area
- State tax agencies and the state Attorney General's office, as each state requires
- The FBI's Internet Crime Complaint Center, for cybercrime
- The Federal Trade Commission, as soon as possible and no later than 30 days after discovery, if unencrypted information of 500 or more consumers is involved
- Local law enforcement
- The Firm's tax software vendor
- The Firm's liability insurance carrier: {{INSURANCE_CARRIER}}
- Legal counsel: {{LEGAL_COUNSEL}}
- Affected clients, to the extent the law and good practice require

First steps: check the EFIN activity report in IRS e-Services for returns the Firm did not file; look for returns transmitted outside office hours; preserve logs; disconnect affected devices from the network without wiping them.

## Attachment D: Employee and contractor acknowledgement

I, ______________________, acknowledge that I have received and been trained on the Written Information Security Plan of {{FIRM_NAME}}, that my questions were answered, and that failure to follow it may result in disciplinary action up to termination.

Signed: ______________________ Date of training: __________ Title: ______________________

## Attachment E: Hardware inventory containing PII

| Hardware item | Location | Principal user | In-service date | Last inventoried |
|---|---|---|---|---|
{{HARDWARE_ROWS}}

## Attachment F: Personnel authorized to access PII

| Name | Role | Job duties | Access level | Date access granted | Date access terminated |
|---|---|---|---|---|---|
{{PERSONNEL_ROWS}}

---

Adapted from the sample plan in IRS Publication 5708, *Creating a Written Information Security Plan for your Tax & Accounting Practice* (Rev. 8-2024), a work of the US government prepared by the Security Summit. This adaptation is not endorsed by the IRS or the Security Summit.
