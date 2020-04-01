def CartesianProduct(a,b,ans,index):
    if index != min(len(a),len(b)) :
        print(ans)
        CartesianProduct(a,b,{a[index],b[index]},index+1)

if __name__ == '__main__':
    a = [1,2,3]
    b = [2,4]
    CartesianProduct(a,b,[],0)
