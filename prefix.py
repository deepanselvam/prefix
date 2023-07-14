
class prefix:
    @staticmethod
    def prefix_sum(array):
        psum=[0]*len(array)
        psum[0]=array[0]
        for i in range(1,len(array)):
            psum[i]=psum[i-1]+array[i]
        return psum
if __name__ == '__main__':
    obj=prefix()
    array=list(map(int,input().split()))
    print(obj.prefix_sum(array))
