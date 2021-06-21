#include<stdio.h>

#define ROWS 3
#define COLS 3

void jacobi(double a[ROWS][COLS], double b[COLS], double chute[COLS], int n){
    for(int it = 0; it < n; it++){
        double temp[COLS];
        for(int i =0; i < ROWS; i++){
            double xi = b[i];
            for(int j=0; j<COLS; j++){
                if(i != j){
                    xi -= a[i][j] * chute[j];
                }
            }
            xi /= a[i][i];
            temp[i] = xi;
        }
        printf("X^(%d) -> ", it + 1);
        for(int k=0; k < COLS; k++){
            chute[k] = temp[k];
            printf("%.10f\t", chute[k]);
        }
        printf("\n");
    }
}
int main(){
    double a[ROWS][COLS] = {{3.55941, 1.6492, 0.66651}, {-1.56294, 4.76155, -1.9549}, {-2.85747, -4.88641, -8.98759}};
    double b[ROWS] = {-2.60175, -4.70056, -0.8796};

    double chute[COLS] = {-3.54628, 4.12575, 3.26808};

    int n = 20;

    jacobi(a, b, chute, n);
}