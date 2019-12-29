class Solution:
    def defangIPaddr(self, address):

        address = address.split('.')

        address = [address[i] + '[.]' if i <
                   len(address)-1 else address[i] for i in range(0, len(address))]

        address = "".join(address)
        return address


obj = Solution()
addr = '255.100.50.0'
ans = obj.defangIPaddr(addr)
print("Final: ", ans)
