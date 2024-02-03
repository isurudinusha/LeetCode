
nums=[1,2,3,4]
res = [1] * (len(nums))  # Initialize a result list with all elements set to 1

for i in range(1, len(nums)):
    res[i] = res[i-1] * nums[i-1]  # Calculate the product of all elements to the left of the current element

postfix = 1
for i in range(len(nums) - 1, -1, -1):
    res[i] *= postfix  # Multiply the product of elements to the left with the product of elements to the right
    postfix *= nums[i]  # Update the product of elements to the right

print(res)

