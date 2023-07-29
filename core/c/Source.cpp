#include "test.h"

int x, y;
double maxs;
int xn1, yn1, xk1, yk1;

double score[8][8] = { 
	{ 16, 15, 14, 13, 8, 7, 6, 5},
	{ 15, 14, 13.5, 12, 8, 7, 6, 5},
	{ 14, 13, 12, 10, 8, 7, 6, 5},
	{ 8, 8, 8, 8, 5.5, 5, 5, 4},
	{ 7, 7, 7, 7, 4.5, 4, 4, 3},
	{ 6, 6, 6, 6, 4, 3.5, 3, 2},
	{ 5, 5, 5, 5, 4, 3, 2, 1},
	{ 4, 4, 4, 4, 3, 2, 1, 0}
};


int mask[8][8] = { 0 };

using namespace std;
void poisk3ch(int yn, int xn, int yk, int xk, int yv, int xv, vector <pair<int, int>> v, int mas[8][8], double sum)
{
	if (yv > 1 && mas[yv - 1][xv] != 0 && mas[yv - 2][xv] == 0)
	{
		bool find = 0;

		for (int i = 0; i < v.size(); i++) if (v[i] == make_pair(yv - 2, xv))
		{
			find = 1;
			break;
		}

		if (find == 0)
		{
			double sc = score[yv - 2][xv] - score[yv][xv];
			if (sum + sc > maxs)
			{
				maxs = sum + sc;
				xn1 = xn;
				yn1 = yn;
				xk1 = xk;
				yk1 = yk;
			}

			swap(mas[yv][xv], mas[yv - 2][xv]);
			v.push_back(make_pair(yv - 2, xv));
			poisk3ch(yn, xn, yk, xk, yv - 2, xv, v, mas, sum + sc);
			swap(mas[yv][xv], mas[yv - 2][xv]);
			v.pop_back();
		}

	}

	if (yv < 6 && mas[yv + 1][xv] != 0 && mas[yv + 2][xv] == 0)
	{
		bool find = 0;

		for (int i = 0; i < v.size(); i++) if (v[i] == make_pair(yv + 2, xv))
		{
			find = 1;
			break;
		}

		if (find == 0)
		{
			double sc = score[yv + 2][xv] - score[yv][xv];
			if (sum + sc > maxs)
			{
				maxs = sum + sc;
				xn1 = xn;
				yn1 = yn;
				xk1 = xk;
				yk1 = yk;
			}

			swap(mas[yv][xv], mas[yv + 2][xv]);
			v.push_back(make_pair(yv + 2, xv));
			poisk3ch(yn, xn, yk, xk, yv + 2, xv, v, mas, sum + sc);
			swap(mas[yv][xv], mas[yv + 2][xv]);
			v.pop_back();
		}
	}

	if (xv > 1 && mas[yv][xv - 1] != 0 && mas[yv][xv - 2] == 0)
	{
		bool find = 0;

		for (int i = 0; i < v.size(); i++) if (v[i] == make_pair(yv, xv - 2))
		{
			find = 1;
			break;
		}

		if (find == 0)
		{
			double sc = score[yv][xv - 2] - score[yv][xv];
			if (sum + sc > maxs)
			{
				maxs = sum + sc;
				xn1 = xn;
				yn1 = yn;
				xk1 = xk;
				yk1 = yk;
			}

			swap(mas[yv][xv], mas[yv][xv - 2]);
			v.push_back(make_pair(yv, xv - 2));
			poisk3ch(yn, xn, yk, xk, yv, xv - 2, v, mas, sum + sc);
			swap(mas[yv][xv], mas[yv][xv - 2]);
			v.pop_back();
		}
	}

	if (xv < 6 && mas[yv][xv + 1] != 0 && mas[yv][xv + 2] == 0)
	{
		bool find = 0;

		for (int i = 0; i < v.size(); i++) if (v[i] == make_pair(yv, xv + 2))
		{
			find = 1;
			break;
		}

		if (find == 0)
		{
			double sc = score[yv][xv + 2] - score[yv][xv];
			if (sum + sc > maxs)
			{
				maxs = sum + sc;
				xn1 = xn;
				yn1 = yn;
				xk1 = xk;
				yk1 = yk;
			}

			swap(mas[yv][xv], mas[yv][xv + 2]);
			v.push_back(make_pair(yv, xv + 2));
			poisk3ch(yn, xn, yk, xk, yv, xv + 2, v, mas, sum + sc);
			swap(mas[yv][xv], mas[yv][xv + 2]);
			v.pop_back();
		}
	}
}

void poisk3(int yn, int xn, int yk, int xk, int mas[8][8], double sum)
{
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			if (mas[i][j] == 2)
			{
				if (i > 0 && mas[i - 1][j] == 0)
				{
					double sc = score[i - 1][j] - score[i][j];
					if (sum + sc > maxs)
					{
						maxs = sum + sc;
						xn1 = xn;
						yn1 = yn;
						xk1 = xk;
						yk1 = yk;
					}
				}
				else if (i > 1 && mas[i - 2][j] == 0) // через клетку
				{
					double sc = score[i - 2][j] - score[i][j];

					if (sum + sc > maxs)
					{
						maxs = sum + sc;
						xn1 = xn;
						yn1 = yn;
						xk1 = xk;
						yk1 = yk;
					}

					vector <pair<int, int>> n;
					n.push_back(make_pair(i, j));
					n.push_back(make_pair(i - 2, j));

					swap(mas[i][j], mas[i - 2][j]);
					poisk3ch(yn, xn, yk, xk, i - 2, j, n, mas, sum + sc);
					swap(mas[i][j], mas[i - 2][j]);
				}

				if (i < 7 && mas[i + 1][j] == 0)
				{
					double sc = score[i + 1][j] - score[i][j];
					if (sum + sc > maxs)
					{
						maxs = sum + sc;
						xn1 = xn;
						yn1 = yn;
						xk1 = xk;
						yk1 = yk;
					}
				}
				else if (i < 6 && mas[i + 2][j] == 0) // через клетку
				{
					double sc = score[i + 2][j] - score[i][j];

					if (sum + sc > maxs)
					{
						maxs = sum + sc;
						xn1 = xn;
						yn1 = yn;
						xk1 = xk;
						yk1 = yk;
					}

					vector <pair<int, int>> n;
					n.push_back(make_pair(i, j));
					n.push_back(make_pair(i + 2, j));

					swap(mas[i][j], mas[i + 2][j]);
					poisk3ch(yn, xn, yk, xk, i + 2, j, n, mas, sum + sc);
					swap(mas[i][j], mas[i + 2][j]);
				}

				if (j > 0 && mas[i][j - 1] == 0)
				{
					double sc = score[i][j - 1] - score[i][j];
					if (sum + sc > maxs)
					{
						maxs = sum + sc;
						xn1 = xn;
						yn1 = yn;
						xk1 = xk;
						yk1 = yk;
					}
				}
				else if (j > 1 && mas[i][j - 2] == 0) // через клетку
				{
					double sc = score[i][j - 2] - score[i][j];

					if (sum + sc > maxs)
					{
						maxs = sum + sc;
						xn1 = xn;
						yn1 = yn;
						xk1 = xk;
						yk1 = yk;
					}

					vector <pair<int, int>> n;
					n.push_back(make_pair(i, j));
					n.push_back(make_pair(i, j - 2));

					swap(mas[i][j], mas[i][j - 2]);
					poisk3ch(yn, xn, yk, xk, i, j - 2, n, mas, sum + sc);
					swap(mas[i][j], mas[i][j - 2]);
				}

				if (j < 7 && mas[i][j + 1] == 0)
				{
					double sc = score[i][j + 1] - score[i][j];
					if (sum + sc > maxs)
					{
						maxs = sum + sc;
						xn1 = xn;
						yn1 = yn;
						xk1 = xk;
						yk1 = yk;
					}
				}
				else if (j < 6 && mas[i][j + 2] == 0) // через клетку
				{
					double sc = score[i][j + 2] - score[i][j];

					if (sum + sc > maxs)
					{
						maxs = sum + sc;
						xn1 = xn;
						yn1 = yn;
						xk1 = xk;
						yk1 = yk;
					}

					vector <pair<int, int>> n;
					n.push_back(make_pair(i, j));
					n.push_back(make_pair(i, j + 2));

					swap(mas[i][j], mas[i][j + 2]);
					poisk3ch(yn, xn, yk, xk, i, j + 2, n, mas, sum + sc);
					swap(mas[i][j], mas[i][j + 2]);
				}
			}
		}
	}
}

void poisk1ch(int yn, int xn, int yv, int xv, vector <pair<int, int>> v, int mas[8][8], double sum)
{
	if (yv > 1 && mas[yv - 1][xv] != 0 && mas[yv - 2][xv] == 0)
	{
		bool find = 0;

		for (int i = 0; i < v.size(); i++) if (v[i] == make_pair(yv - 2, xv))
		{
			find = 1;
			break;
		}

		if (find == 0)
		{
			double sc = score[yv - 2][xv] - score[yv][xv];
			if (sum + sc >= maxs)
			{
				maxs = sum + sc;
				yn1 = yn;
				xn1 = xn;
				yk1 = yv - 2;
				xk1 = xv;
			}

			swap(mas[yv][xv], mas[yv - 2][xv]);
			v.push_back(make_pair(yv - 2, xv));
			poisk3(yn, xn, yv - 2, xv, mas, sum + sc);
			poisk1ch(yn, xn, yv - 2, xv, v, mas, sum + sc);
			swap(mas[yv][xv], mas[yv - 2][xv]);
			v.pop_back();
		}

	}

	if (yv < 6 && mas[yv + 1][xv] != 0 && mas[yv + 2][xv] == 0)
	{
		bool find = 0;

		for (int i = 0; i < v.size(); i++) if (v[i] == make_pair(yv + 2, xv))
		{
			find = 1;
			break;
		}

		if (find == 0)
		{
			double sc = score[yv + 2][xv] - score[yv][xv];
			if (sum + sc >= maxs)
			{
				maxs = sum + sc;
				yn1 = yn;
				xn1 = xn;
				yk1 = yv + 2;
				xk1 = xv;
			}

			swap(mas[yv][xv], mas[yv + 2][xv]);
			v.push_back(make_pair(yv + 2, xv));
			poisk3(yn, xn, yv + 2, xv, mas, sum + sc);
			poisk1ch(yn, xn, yv + 2, xv, v, mas, sum + sc);
			swap(mas[yv][xv], mas[yv + 2][xv]);
			v.pop_back();
		}
	}

	if (xv > 1 && mas[yv][xv - 1] != 0 && mas[yv][xv - 2] == 0)
	{
		bool find = 0;

		for (int i = 0; i < v.size(); i++) if (v[i] == make_pair(yv, xv - 2))
		{
			find = 1;
			break;
		}

		if (find == 0)
		{
			double sc = score[yv][xv - 2] - score[yv][xv];
			if (sum + sc >= maxs)
			{
				maxs = sum + sc;
				yn1 = yn;
				xn1 = xn;
				yk1 = yv;
				xk1 = xv - 2;
			}

			swap(mas[yv][xv], mas[yv][xv - 2]);
			v.push_back(make_pair(yv, xv - 2));
			poisk3(yn, xn, yv, xv - 2, mas, sum + sc);
			poisk1ch(yn, xn, yv, xv - 2, v, mas, sum + sc);
			swap(mas[yv][xv], mas[yv][xv - 2]);
			v.pop_back();
		}
	}

	if (xv < 6 && mas[yv][xv + 1] != 0 && mas[yv][xv + 2] == 0)
	{
		bool find = 0;

		for (int i = 0; i < v.size(); i++) if (v[i] == make_pair(yv, xv + 2))
		{
			find = 1;
			break;
		}

		if (find == 0)
		{
			double sc = score[yv][xv + 2] - score[yv][xv];
			if (sum + sc >= maxs)
			{
				maxs = sum + sc;
				yn1 = yn;
				xn1 = xn;
				yk1 = yv;
				xk1 = xv + 2;
			}

			swap(mas[yv][xv], mas[yv][xv + 2]);
			v.push_back(make_pair(yv, xv + 2));
			poisk3(yn, xn, yv, xv + 2, mas, sum + sc);
			poisk1ch(yn, xn, yv, xv + 2, v, mas, sum + sc);
			swap(mas[yv][xv], mas[yv][xv + 2]);
			v.pop_back();
		}
	}
}

void poisk1(int mas[8][8])
{
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			if (mas[i][j] == 2)
			{
				if (i > 0 && mas[i - 1][j] == 0)
				{
					double sc = score[i - 1][j] - score[i][j];
					if (sc >= maxs)
					{
						maxs = sc;
						yn1 = i;
						xn1 = j;
						yk1 = i - 1;
						xk1 = j;
					}

					swap(mas[i][j], mas[i - 1][j]);
					poisk3(i, j, i - 1, j, mas, sc);
					swap(mas[i][j], mas[i - 1][j]);
				}
				else if (i > 1 && mas[i - 2][j] == 0) // через клетку
				{
					vector <pair<int, int>> n;
					n.push_back(make_pair(i, j));
					n.push_back(make_pair(i - 2, j));

					double sc = score[i - 2][j] - score[i][j];
					if (sc >= maxs)
					{
						maxs = sc;
						yn1 = i;
						xn1 = j;
						yk1 = i - 2;
						xk1 = j;
					}

					swap(mas[i][j], mas[i - 2][j]);
					poisk3(i, j, i - 2, j, mas, sc);
					poisk1ch(i, j, i - 2, j, n, mas, sc);
					swap(mas[i][j], mas[i - 2][j]);
				}

				if (i < 7 && mas[i + 1][j] == 0)
				{
					double sc = score[i + 1][j] - score[i][j];
					if (sc >= maxs)
					{
						maxs = sc;
						yn1 = i;
						xn1 = j;
						yk1 = i + 1;
						xk1 = j;
					}

					swap(mas[i][j], mas[i + 1][j]);
					poisk3(i, j, i + 1, j, mas, sc);
					swap(mas[i][j], mas[i + 1][j]);
				}
				else if (i < 6 && mas[i + 2][j] == 0) // через клетку
				{
					vector <pair<int, int>> n;
					n.push_back(make_pair(i, j));
					n.push_back(make_pair(i + 2, j));

					double sc = score[i + 2][j] - score[i][j];
					if (sc >= maxs)
					{
						maxs = sc;
						yn1 = i;
						xn1 = j;
						yk1 = i + 2;
						xk1 = j;
					}

					swap(mas[i][j], mas[i + 2][j]);
					poisk3(i, j, i + 2, j, mas, sc);
					poisk1ch(i, j, i + 2, j, n, mas, sc);
					swap(mas[i][j], mas[i + 2][j]);
				}

				if (j > 0 && mas[i][j - 1] == 0)
				{
					double sc = score[i][j - 1] - score[i][j];
					if (sc >= maxs)
					{
						maxs = sc;
						yn1 = i;
						xn1 = j;
						yk1 = i;
						xk1 = j - 1;
					}

					swap(mas[i][j], mas[i][j - 1]);
					poisk3(i, j, i, j - 1, mas, sc);
					swap(mas[i][j], mas[i][j - 1]);
				}
				else if (j > 1 && mas[i][j - 2] == 0) // через клетку
				{
					vector <pair<int, int>> n;
					n.push_back(make_pair(i, j));
					n.push_back(make_pair(i, j - 2));

					double sc = score[i][j - 2] - score[i][j];
					if (sc >= maxs)
					{
						maxs = sc;
						yn1 = i;
						xn1 = j;
						yk1 = i;
						xk1 = j - 2;
					}

					swap(mas[i][j], mas[i][j - 2]);
					poisk3(i, j, i, j - 2, mas, sc);
					poisk1ch(i, j, i, j - 2, n, mas, sc);
					swap(mas[i][j], mas[i][j - 2]);
				}

				if (j < 7 && mas[i][j + 1] == 0)
				{
					double sc = score[i][j + 1] - score[i][j];
					if (sc >= maxs)
					{
						maxs = sc;
						yn1 = i;
						xn1 = j;
						yk1 = i;
						xk1 = j + 1;
					}

					swap(mas[i][j], mas[i][j + 1]);
					poisk3(i, j, i, j + 1, mas, sc);
					swap(mas[i][j], mas[i][j + 1]);
				}
				else if (j < 6 && mas[i][j + 2] == 0) // через клетку
				{
					vector <pair<int, int>> n;
					n.push_back(make_pair(i, j));
					n.push_back(make_pair(i, j + 2));

					double sc = score[i][j + 2] - score[i][j];
					if (sc >= maxs)
					{
						maxs = sc;
						yn1 = i;
						xn1 = j;
						yk1 = i;
						xk1 = j + 2;
					}
					swap(mas[i][j], mas[i][j + 2]);
					poisk3(i, j, i, j + 2, mas, sc);
					poisk1ch(i, j, i, j + 2, n, mas, sc);
					swap(mas[i][j], mas[i][j + 2]);
				}
			}
		}
	}
}

void search_hard_available_moves(int field_with_figures[8][8], int xs, int ys) {
	if (xs - 2 >= 0) {
		if (field_with_figures[ys][xs - 2] == 0 && field_with_figures[ys][xs - 1] != 0 && field_with_figures[ys][xs - 2] != 9 && field_with_figures[ys][xs - 1] != 9) {
			field_with_figures[ys][xs - 2] = 9;
			search_hard_available_moves(field_with_figures, xs - 2, ys);
		}
	}
	if (xs + 2 < 8) {
		if (field_with_figures[ys][xs + 2] == 0 && field_with_figures[ys][xs + 1] != 0 && field_with_figures[ys][xs + 2] != 9 && field_with_figures[ys][xs + 1] != 9) {
			field_with_figures[ys][xs + 2] = 9;

			search_hard_available_moves(field_with_figures, xs + 2, ys);
		}

	}
	if (ys - 2 >= 0) {
		if (field_with_figures[ys - 2][xs] == 0 && field_with_figures[ys - 1][xs] != 0 && field_with_figures[ys - 2][xs] != 9 && field_with_figures[ys - 1][xs] != 9) {
			field_with_figures[ys - 2][xs] = 9;
			search_hard_available_moves(field_with_figures, xs, ys - 2);
		}
	}
	if (ys + 2 < 8) {
		if (field_with_figures[ys + 2][xs] == 0 && field_with_figures[ys + 1][xs] != 0 && field_with_figures[ys + 2][xs] != 9 && field_with_figures[ys + 1][xs] != 9) {
			field_with_figures[ys + 2][xs] = 9;
			search_hard_available_moves(field_with_figures, xs, ys + 2);
		}
	}
}

void search_available_moves(int field_with_figures[8][8], int x, int y) {
	if (field_with_figures[y][x] == 1)
		field_with_figures[y][x] = 8;
	if (field_with_figures[y][x] == 2)
		field_with_figures[y][x] = 7;
	if (x - 1 >= 0) {
		if (field_with_figures[y][x - 1] == 0) {
			field_with_figures[y][x - 1] = 9;
		}

	}
	if (x + 1 < 8) {
		if (field_with_figures[y][x + 1] == 0) {
			field_with_figures[y][x + 1] = 9;
		}

	}
	if (y - 1 >= 0) {
		if (field_with_figures[y - 1][x] == 0) {
			field_with_figures[y - 1][x] = 9;
		}

	}
	if (y + 1 < 8) {
		if (field_with_figures[y + 1][x] == 0) {
			field_with_figures[y + 1][x] = 9;
		}
	}
	search_hard_available_moves(field_with_figures, x, y);

}

int *search_move(int arr[64], int x, int y) {
	int arr2d[8][8]; // создаем целевой двумерный массив с 8 строками и 8 столбцами

	// заполняем массив arr2d из массива arr
	for (int i = 0; i < 8; i++) {
	  for (int j = 0; j < 8; j++) {
	    arr2d[i][j] = arr[i * 8 + j];
	  }
	}
	search_available_moves(arr2d, x, y);
	int *array = (int*) malloc(64 * sizeof(int));
    int k = 0;
	    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            array[k] = arr2d[i][j];
            k++;
        }
    }
	return array;
}

int *ai_move(int arr[64]) {
	int arr2d[8][8]; // создаем целевой двумерный массив с 8 строками и 8 столбцами

	// заполняем массив arr2d из массива arr
	for (int i = 0; i < 8; i++) {
	  for (int j = 0; j < 8; j++) {
	    arr2d[i][j] = arr[i * 8 + j];
	  }
	}
	maxs = -100;
	poisk1(arr2d);
	swap(arr2d[yn1][xn1], arr2d[yk1][xk1]);
	int *array = (int*) malloc(64 * sizeof(int));
    int k = 0;
	    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            array[k] = arr2d[i][j];
            k++;
        }
    }
	return array;
}