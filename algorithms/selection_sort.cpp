#include <iostream>
//#include <utility>

void swap (double &first, double &second){
    double temp {first};
    first = second;
    second = temp;
    return;
}
)

void selection_sort(double array[], std::size_t capacity){
    // find the index of the maximum
    // entry between indicies 0 and 'k'
    // then, swapp that entry with k.
    std::size_t max_index{0};
    for (size_t k{capacity - 1}; k > 0; --k){
        std::size_t max_index{find_maxx(array, k + 1)};
        

    
}