#include <iostream>

using namespace std;    // for å slippe å skrive std:: foran cout, cin, endl

// Først lager vi selve spill-brettet, 3x3. Dette er en 2D array
char board[3][3] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};

char marker;    // Markerer hvilken spiller sin tur det er
int player;     // Markerer hvilken spiller sin tur det er


// Funksjonen som printer ut brettet.
void printBoard() {
    cout << endl;
    cout << " " << board[0][0] << " | " << board[0][1] << " | " << board[0][2] << endl;
    cout << "---+---+---" << endl;
    cout << " " << board[1][0] << " | " << board[1][1] << " | " << board[1][2] << endl;
    cout << "---+---+---" << endl;
    cout << " " << board[2][0] << " | " << board[2][1] << " | " << board[2][2] << endl;
    cout << endl;
}

// Funksjon som sørger for at man kan plassere sin marker på brettet
bool placeMarker(int slot) {
    int row = slot / 3; // Finner riktig rad
    int col;            // Finner riktig kolonne

    if(slot % 3 == 0) { // Hvis slot er delelig på 3, så er det en ny rad
        row = row - 1;  // Vi må trekke fra 1 fra raden, fordi vi starter på 0
        col = 2;        // Vi setter kolonnen til 2, fordi vi starter på 0
    }
    else {
        col = (slot % 3) - 1;
    }

    // Hvis det er ledig plass, så plasserer vi markøren
    if(board[row][col] != 'X' && board[row][col] != 'O') {
        board[row][col] = marker;
        return true;
    }
    else {
        return false;
    }
}

// Funksjonen som sjekker om noen har vunnet
int winner() {
    for(int i = 0; i < 3; i++) {
        // Sjekker om noen har vunnet på rad
        if(board[i][0] == board[i][1] && board[i][1] == board[i][2]) return player;
        // Sjekker om noen har vunnet på kolonne
        if(board[0][i] == board[1][i] && board[1][i] == board[2][i]) return player;

    }
    // Sjekker om noen har vunnet på diagonal
    if(board[0][0] == board[1][1] && board[1][1] == board[2][2]) return player;
    if(board[0][2] == board[1][1] && board[1][1] == board[2][0]) return player;
    return 0;
}


// Funksjon som bytter spiller, slik at de spiller annenhver gang
void swap_player_and_marker() {
    if(marker == 'X') marker = 'O';
    else marker = 'X';

    if(player == 1) player = 2;
    else player = 1;
}

// Funksjonen som kjører selve spillet
void game() {
    cout << "Velg din markør, X eller O: ";
    char marker_p1;
    cin >> marker_p1;

    player = 1;
    marker = marker_p1;

    printBoard();

    int player_won;

    // Spillet kjører så lenge ingen har vunnet
    for(int i = 0; i < 9; i++) {
        cout << "Det er spiller " << player << " sin tur: ";
        int slot;
        cin >> slot;

        // Dersom man velger et tall utenfor 1-9
        if(slot < 1 || slot > 9) {
            cout << "Ugyldig valg. Velg mellom 1 og 9 :)\n" << endl;
            i--;
            continue;
        }

        // Dersom man velger en slot som allerede er valgt, må vi trekke fra et move fra i, for å
        // unngå at spillet blir avsluttet for tidlig. (Ett feil move blir inntil nå også telt).
        if(!placeMarker(slot)) {
            cout << "Ups! Denne er allerede valgt! Velg en annen plass :)\n" << endl;
            i--;
            continue;
        }
        printBoard();

        player_won = winner();

        if(player_won == 1) {
            cout << "Spiller 1 vant!\n\n"; break;
        }
        else if(player_won == 2) {
            cout << "Spiller 2 vant!\n\n"; break;
        }

        swap_player_and_marker();   // Bytter spiller
    }

    if(player_won == 0) cout << "Ingen vant, det ble uavgjort...\n\n" << endl;
}


int main() {
    game();
}
