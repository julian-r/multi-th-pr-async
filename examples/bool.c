
typedef int bool;
#define true 1
#define false 0

void set_bool(bool* x) {
    *x = true;
}

void free_bool(bool* x) {
    *x = false;
}


int main() {
    bool a = true;

    for(int i=0; i<1000000000; ++i) {
        set_bool(&a);
        free_bool(&a);
    }
}