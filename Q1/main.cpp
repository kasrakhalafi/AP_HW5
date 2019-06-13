#include<iostream>
#include <vector>
#include <algorithm>


int main(){
/////////////////////// A //////////////////////////////
    std::vector<int> vec1(100);
    std::vector<int> vec2(10);
    std::for_each(vec1.begin(), vec1.end(), [](int &i) { i = rand() % 100 + 1; });
    std::for_each(vec2.begin(), vec2.end(), [](int &i) { i = rand() % 10 + 1; });

////////////////////// B //////////////////////////////////
    std::copy(vec1.begin(), vec1.end(), back_inserter(vec2));
    std::cout << "vec1 "<< std::endl;
    for(auto x:vec1) {
        static int i{};
        std::cout << i++ << " :" << x << std::endl;
    }

    std::cout << "vec2 "<< std::endl;
    for(auto x:vec2) {
        static int i{};
        std::cout << i++ << " :" << x << std::endl;
    }

////////////////////// C //////////////////////////////////
    std::vector<int> odd_vec(vec1.size());
    auto it = std::copy_if (vec1.begin(), vec1.end(), odd_vec.begin(), [](int i){return i%2==1;} );
    odd_vec.resize(std::distance(odd_vec.begin(),it));  // shrink container to new size
    //std::for_each(vec1.begin(), vec1.end(), []() { i = rand() % 10 + 1; });
    std::cout << "vec3 "<< std::endl;
    for(auto x:odd_vec) {
        static int i{};
        std::cout << i++ << " :" << x << std::endl;
    }

////////////////////// D ///////////////////////////////////
    std::vector<int> reverse_vec(vec1.rbegin(),vec1.rend());
    std::cout << "reverse vec "<< std::endl;
    for(auto x:reverse_vec) {
        static int i{};
        std::cout << i++ << " :" << x << std::endl;
    }

///////////////////// E /////////////////////////////////////
    int x = 0;
    int a[] = {1,2};
    //// EXECUTION WAS NOT ADDED!! ////////////////
    //std::for_each(std::execution::par, std::begin(a), std::end(a), [&](int) {
    //});
    return 0;

}
