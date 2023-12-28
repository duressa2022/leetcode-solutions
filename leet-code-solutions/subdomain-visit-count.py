class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash_domain={}
        for path in cpdomains:
            number,domain=path.split()
            do_list=domain.split(".")
            for i in range(len(do_list)):
                sub_domain=".".join(do_list[i:])
                if sub_domain not in hash_domain:
                    hash_domain[sub_domain]=int(number)
                else:
                    hash_domain[sub_domain]+=int(number)
        result=[str(hash_domain[key])+" "+key for key in hash_domain]
        return result
        