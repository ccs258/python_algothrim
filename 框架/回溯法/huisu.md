"""
List<List<Integer>> res = new LinkedList<>();

/* 主函数，输入一组不重复的数字，返回它们的全排列 */
List<List<Integer>> permute(int[] nums) {
    // 记录「路径」
    LinkedList<Integer> track = new LinkedList<>();
    backtrack(nums, track);
    return res;
}

// 路径：记录在 track 中
// 选择列表：nums 中不存在于 track 的那些元素
// 结束条件：nums 中的元素全都在 track 中出现
void backtrack(int[] nums, LinkedList<Integer> track) {
    // 触发结束条件
    if (track.size() == nums.length) {
        res.add(new LinkedList(track));
        return;
    }

    for (int i = 0; i < nums.length; i++) {
        // 排除不合法的选择
        if (track.contains(nums[i]))
            continue;
        // 做选择
        track.add(nums[i]);
        // 进入下一层决策树
        backtrack(nums, track);
        // 取消选择
        track.removeLast();   ##自我理解：这个地方是清除当前选择路径，回溯到商议节点，选择其他节点；
        比如，1,2,3；根节点是2，现在选择了（2,1）作为路径，进行进一步回溯，计算得到结果；
        回溯到路径中只含2，再根据for循环遍历取到下一节点，（2,3），再进行下一步的计算
    }
}
"""

#总结
    回溯法需要考虑的是：
    路径：即当前的结果集；
    选择：即当前可供选择作为结果的集合；
    回溯判断，有3种：
    已经存在路径的结果，跳过，进行下一轮计算；
    计算一轮之后，需要进行路径的回溯，以便方便下一轮计算；
    如果可供选择的集合已经取完，则返回结果