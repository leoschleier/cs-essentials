#include <stdio.h>
#include <string.h>

int* mergesort(int* sorted, int* elements, size_t count);
int* merge(int* merged, int* left, int* right, size_t leftCount, size_t rightCount);
void printArr(char* text, int* arr, size_t count);


int main() { 
    printf("Starting mergesort.\n");
    int elements[] = {13, 11, 12, 5, 6, 7};
    size_t count = sizeof(elements) / sizeof(*elements);
    int sorted[count];

    mergesort(sorted, elements, count);

    return 0;
}


void printArr(char* text, int* arr, size_t count){
   printf("%s",  text);
   printf("[");

   int indexLast = count - 1;

   if (indexLast >= 0){
        for(int i=0; i<indexLast; i++){
            printf("%i, ", arr[i]);
    }
        printf("%d", arr[indexLast]);
   }
   printf("]\n");
}


int* mergesort(int* sorted, int* elements, size_t count) {
    printArr("Sorting: ", elements, count);
    
    if (count <= 1){
        memcpy(sorted, elements, sizeof(int));
        printArr("Sorted: ", sorted, count);
        return sorted;
    }

    // Split elements into two halves.
    int mid = (int) count / 2;
    int leftCount = mid, rightCount = count-mid;
    int *leftHalf = elements, *rightHalf = elements + mid;

    // Apply mergesort on each half.
    int leftSorted[leftCount], rightSorted[rightCount];
    mergesort(leftSorted, leftHalf, leftCount);
    mergesort(rightSorted, rightHalf, rightCount);

    // Merge the two halves.
    merge(sorted, leftSorted, rightSorted, leftCount, rightCount);
    printArr("Sorted: ", sorted, count);
    return sorted;  
}


int* merge(int* merged, int* left, int* right, size_t leftCount, size_t rightCount) {
    int leftOffset = 0, offset = 0, idx = 0;
    for(int l=0; l<leftCount; l++){
        for(int r=offset; r<rightCount; r++){
            if(left[l] <= right[r]){
                merged[idx] = left[l];
                idx ++;
                leftOffset ++; 
                break;
            }
            merged[idx] = right[r];
            idx ++;
            offset++;
        }
    }
    for(int l=leftOffset; l<leftCount; l++){
        merged[idx] = left[l];
        idx++;
    }
    for(int r= offset; r<rightCount; r++){
        merged[idx] = right[r];
        idx++;
    }

    return merged;
}
