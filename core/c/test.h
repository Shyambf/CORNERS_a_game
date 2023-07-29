#ifndef _TEST_H_
#define _TEST_H_
#include <iostream>
#include <vector>

#ifdef  __cplusplus
extern "C" {
#endif

#include <stdio.h>
#include <string>
#include <stdlib.h> 

int* search_move(int arr[64], int x, int y);
int* ai_move(int arr[64]);

#ifdef  __cplusplus
}
#endif

#endif  /* _TEST_H_ */
