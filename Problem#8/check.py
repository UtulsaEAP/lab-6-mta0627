'''
Name: Mason Anderson
Time: 3/8/24 4:39 PM
'''

def in_order(nums):
    # Type your code here.

    sorted_nums = nums.copy() 
    sorted_nums.sort()
    
    if nums == sorted_nums:
        return True
    else:
        return False

if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
