# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains_count={}
        ans = []
        for i in range(len(cpdomains)):
            cp=cpdomains[i].split(" ")
            domains=cp[1].split(".")
            if len(domains)==3:
                temp1=domains[2]
                domains_count[temp1]=domains_count.get(temp1,0)+int(cp[0])
                temp2=".".join(domains[1:])
                domains_count[temp2]=domains_count.get(temp2,0)+int(cp[0])
                temp3=".".join(domains[0:])
                domains_count[temp3]=domains_count.get(temp3,0)+int(cp[0])
            else:
                temp2=".".join(domains[1:])
                domains_count[temp2]=domains_count.get(temp2,0)+int(cp[0])
                temp3=".".join(domains[0:])
                domains_count[temp3]=domains_count.get(temp3,0)+int(cp[0])
        for key, value in domains_count.items():
            ans.append(str(value)+" "+key)
        return ans