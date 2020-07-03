



def solution(nums,track,rst):
    if len(nums) == len(track):
        # print("track is ",track)
        rst.append(track)
        print("rst is ",rst)
        return track
    for i in nums:
        if  i in track:
            continue
        else:
            track.append(i)
            # print("after append track is ",track)
            solution(nums,track,rst)
            track.remove(i)
            # print("after remove track is ",track)

if __name__ == '__main__':
    nums = [1,2,3]
    track = []
    rst = []
    solution(nums,track,rst)

    """
    after append track is  [1]
after append track is  [1, 2]
after append track is  [1, 2, 3]
track is  [1, 2, 3]
after remove track is  [1, 2]
after remove track is  [1]
after append track is  [1, 3]
after append track is  [1, 3, 2]
track is  [1, 3, 2]
after remove track is  [1, 3]
after remove track is  [1]
after remove track is  []
after append track is  [2]
after append track is  [2, 1]
after append track is  [2, 1, 3]
track is  [2, 1, 3]
after remove track is  [2, 1]
after remove track is  [2]
after append track is  [2, 3]
after append track is  [2, 3, 1]
track is  [2, 3, 1]
after remove track is  [2, 3]
after remove track is  [2]
after remove track is  []
after append track is  [3]
after append track is  [3, 1]
after append track is  [3, 1, 2]
track is  [3, 1, 2]
after remove track is  [3, 1]
after remove track is  [3]
after append track is  [3, 2]
after append track is  [3, 2, 1]
track is  [3, 2, 1]
after remove track is  [3, 2]
after remove track is  [3]
after remove track is  []
    
    """