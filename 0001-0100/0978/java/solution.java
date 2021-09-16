class Solution {
    public int maxTurbulenceSize(int[] arr) {
        int checkGreater = checkArr(arr, true);
        int checkLesser = checkArr(arr, false);
        
        if (checkGreater > checkLesser) {
            return checkGreater;
        } else {
            return checkLesser;
        }
    }
    
    public int checkArr(int[] arr, boolean checkGreater) {
        if (arr.length == 1) {
            return 1;
        }
        
        int maxTurb = 0;
        int currTurb = 1;
        
        for (int i=0; i<arr.length; ++i) {
            if (i != arr.length-1) {
                if (checkGreater) {
                    checkGreater = !checkGreater;
                    if (arr[i] > arr[i+1]) {
                        currTurb += 1;
                    } else {
                        if (currTurb > maxTurb) {
                            maxTurb = currTurb;
                        }
                        currTurb = 1;
                    }
                } else {
                    checkGreater = !checkGreater;
                    if (arr[i] < arr[i+1]) {
                        currTurb += 1;
                    } else {
                        if (currTurb > maxTurb) {
                            maxTurb = currTurb;
                        }
                        currTurb = 1;
                    }
                }
            } else {
                if (checkGreater) {
                    if (arr[i] < arr[i-1]) {
                        currTurb += 1;
                    }
                } else {
                    if (arr[i] > arr[i-1]) {
                        currTurb += 1;
                    }
                }
                
                if (currTurb > maxTurb) {
                    maxTurb = currTurb;
                }
            }
        }
        
        return maxTurb;
    }
}