function longestCommonPrefix(strs: string[]): string {
    for (let i = 0; i < strs.length; i++) {
        // const element = strs[i];
        for (let j = 0; j < strs[i].length; j++) {
            const element = strs[i][j];
            console.log(element);
        }
    }
};

longestCommonPrefix(["flower","flow","flight"]) 