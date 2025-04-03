# Security Policy

## Supported Versions

We only support the latest version of PyHTML, but are open to backporting 
security fixes to earlier versions on-request.

## Reporting a Vulnerability

We take the security of PyHTML very seriously. If you have discovered a 
vulnerability in PyHTML, please disclose it responsibly.

Some vulnerabilities we consider to be high-severity are:

* Bugs where HTML, JS or CSS code can be embedded within PyHTML output
  without making use of the `p.style`, p.DangerousRawHtml` or `p.script`
  tags.
* Bugs where the act of rendering PyHTML can trigger remote code execution
  given seemingly-correct input (eg a `str` or descendant of `p.Tag`).

You should disclose these vulnerabilities by creating a private issue on 
the project's GitHub repo. We will aim to fix these issues as quickly as 
possible.
