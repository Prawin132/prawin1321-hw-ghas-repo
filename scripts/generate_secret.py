
import rstr

print(f"AWS_KEYID: {rstr.xeger(r'AKIA[A-Z2-7]{16}')}")
print(f"AWS_SECRET: {rstr.xeger(r'[0-9A-Za-z/+=]{40}')}")
print(f"DATADOG_TOKEN: {rstr.xeger(r'[a-f0-9]{32}|[a-f0-9]{40}')}")
ptint(f"GitHubToken:github_pat_wt6lVzza0QFx/U33PU8DrkMbnKiu+bv9jheR0h)
