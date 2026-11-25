"""Simulasi NFA, DFA, dan konversi NFA ke DFA.

Contoh bawaan mengikuti materi: NFA menerima string yang diawali 0 dan
memiliki setidaknya satu 1 setelahnya (bentuk 0+1(0|1)*).
Jalankan dengan: python automata.py
"""

from collections import deque
from dataclasses import dataclass
from typing import Dict, FrozenSet, Iterable, List, Set, Tuple


State = str
Symbol = str
TransitionKey = Tuple[State, Symbol]


@dataclass
class Automaton:
    states: Set[State]
    alphabet: List[Symbol]
    start: State
    finals: Set[State]
    transitions: Dict[TransitionKey, Set[State]]

    def destinations(self, state: State, symbol: Symbol) -> Set[State]:
        """Return all destinations (one for DFA, possibly many for NFA)."""
        return self.transitions.get((state, symbol), set())


def make_example_nfa() -> Automaton:
    """Build the NFA from the course slides (alphabet {0, 1})."""
    return Automaton(
        states={"q0", "q1", "q2"},
        alphabet=["0", "1"],
        start="q0",
        finals={"q2"},
        transitions={
            ("q0", "0"): {"q0", "q1"},
            ("q1", "1"): {"q1", "q2"},
            ("q2", "0"): {"q2"},
            ("q2", "1"): {"q2"},
        },
    )


def format_set(states: Iterable[State]) -> str:
    values = sorted(states)
    return "{" + (", ".join(values) if values else "∅") + "}"


def simulate_nfa(machine: Automaton, word: str, show_steps: bool = True) -> bool:
    """Simulate an NFA by tracking all active states after each symbol."""
    active = {machine.start}
    if show_steps:
        print(f"  Mulai di {format_set(active)}")

    for position, symbol in enumerate(word, start=1):
        if symbol not in machine.alphabet:
            raise ValueError(
                f"Simbol '{symbol}' tidak termasuk alfabet {machine.alphabet}."
            )
        next_states: Set[State] = set()
        for state in active:
            next_states.update(machine.destinations(state, symbol))
        active = next_states
        if show_steps:
            print(f"  Baca '{symbol}' (posisi {position}) -> {format_set(active)}")

    accepted = bool(active & machine.finals)
    if show_steps:
        print(f"  State final NFA: {format_set(machine.finals)}")
        print(f"  Hasil: {'DITERIMA' if accepted else 'DITOLAK'}")
    return accepted


def convert_nfa_to_dfa(
    nfa: Automaton,
) -> Tuple[Automaton, Dict[FrozenSet[State], str]]:
    """Convert an NFA without epsilon transitions using subset construction."""
    start_subset = frozenset({nfa.start})
    subsets = [start_subset]
    names: Dict[FrozenSet[State], str] = {start_subset: "S0"}
    transitions: Dict[TransitionKey, Set[State]] = {}
    queue = deque([start_subset])

    while queue:
        current = queue.popleft()
        current_name = names[current]

        for symbol in nfa.alphabet:
            destination_subset: Set[State] = set()
            for state in current:
                destination_subset.update(nfa.destinations(state, symbol))
            destination_key = frozenset(destination_subset)

            if destination_key not in names:
                names[destination_key] = f"S{len(names)}"
                subsets.append(destination_key)
                queue.append(destination_key)

            transitions[(current_name, symbol)] = {names[destination_key]}

    dfa_states = set(names.values())
    dfa_finals = {
        names[subset]
        for subset in subsets
        if subset & nfa.finals
    }
    dfa = Automaton(
        states=dfa_states,
        alphabet=list(nfa.alphabet),
        start=names[start_subset],
        finals=dfa_finals,
        transitions=transitions,
    )
    return dfa, names


def simulate_dfa(machine: Automaton, word: str, show_steps: bool = True) -> bool:
    """Simulate a DFA, reporting the single current state at each step."""
    current = machine.start
    if show_steps:
        print(f"  Mulai di {current}")

    for position, symbol in enumerate(word, start=1):
        if symbol not in machine.alphabet:
            raise ValueError(
                f"Simbol '{symbol}' tidak termasuk alfabet {machine.alphabet}."
            )
        destinations = machine.destinations(current, symbol)
        if len(destinations) != 1:
            raise ValueError(
                f"Transisi DFA dari {current} dengan '{symbol}' harus punya satu tujuan."
            )
        current = next(iter(destinations))
        if show_steps:
            print(f"  Baca '{symbol}' (posisi {position}) -> {current}")

    accepted = current in machine.finals
    if show_steps:
        print(f"  Berakhir di {current}; state final: {format_set(machine.finals)}")
        print(f"  Hasil: {'DITERIMA' if accepted else 'DITOLAK'}")
    return accepted


def print_dfa_table(dfa: Automaton, subset_names: Dict[FrozenSet[State], str]) -> None:
    """Print the DFA transition table, including the NFA subset per DFA state."""
    subset_for_name = {name: subset for subset, name in subset_names.items()}
    headings = ["State DFA", "Kumpulan state NFA", *dfa.alphabet, "Status"]
    rows = []
    for state in sorted(dfa.states, key=lambda item: int(item[1:])):
        destinations = [
            next(iter(dfa.destinations(state, symbol)))
            for symbol in dfa.alphabet
        ]
        status = []
        if state == dfa.start:
            status.append("Awal")
        if state in dfa.finals:
            status.append("Final")
        rows.append(
            [state, format_set(subset_for_name[state]), *destinations, ", ".join(status) or "—"]
        )

    widths = [max(len(str(row[column])) for row in [headings, *rows]) for column in range(len(headings))]
    print("  " + " | ".join(str(value).ljust(widths[index]) for index, value in enumerate(headings)))
    print("  " + "-+-".join("-" * width for width in widths))
    for row in rows:
        print("  " + " | ".join(str(value).ljust(widths[index]) for index, value in enumerate(row)))


def print_nfa() -> None:
    print("\nNFA contoh")
    print("  State       : q0, q1, q2")
    print("  Alfabet     : 0, 1")
    print("  State awal  : q0")
    print("  State final : q2")
    print("  Bahasa      : string diawali 0 dan memiliki setidaknya satu 1 setelahnya")
    print("  Transisi:")
    print("    δ(q0, 0) = {q0, q1}    δ(q0, 1) = ∅")
    print("    δ(q1, 0) = ∅           δ(q1, 1) = {q1, q2}")
    print("    δ(q2, 0) = {q2}")
    print("    δ(q2, 1) = {q2}")


def ask_word() -> str:
    return input("Masukkan string biner (kosongkan untuk string kosong): ").strip()


def main() -> None:
    nfa = make_example_nfa()
    dfa, subset_names = convert_nfa_to_dfa(nfa)

    print("=" * 62)
    print(" SIMULASI NFA, DFA, DAN KONVERSI NFA KE DFA")
    print("=" * 62)
    print_nfa()
    print("\nDFA hasil konversi (konstruksi himpunan bagian)")
    print_dfa_table(dfa, subset_names)

    while True:
        print("\nMenu:")
        print("  1. Simulasikan string pada NFA")
        print("  2. Simulasikan string pada DFA hasil konversi")
        print("  3. Bandingkan NFA dan DFA untuk satu string")
        print("  0. Keluar")
        choice = input("Pilih menu: ").strip()

        if choice == "0":
            print("Program selesai.")
            break
        if choice not in {"1", "2", "3"}:
            print("Pilihan tidak tersedia. Silakan pilih 1, 2, 3, atau 0.")
            continue

        word = ask_word()
        try:
            if choice == "1":
                print("\nLangkah simulasi NFA:")
                simulate_nfa(nfa, word)
            elif choice == "2":
                print("\nLangkah simulasi DFA:")
                simulate_dfa(dfa, word)
            else:
                print("\nLangkah simulasi NFA:")
                nfa_result = simulate_nfa(nfa, word)
                print("\nLangkah simulasi DFA:")
                dfa_result = simulate_dfa(dfa, word)
                print("\nPemeriksaan kesetaraan:")
                print(f"  NFA: {'diterima' if nfa_result else 'ditolak'}")
                print(f"  DFA: {'diterima' if dfa_result else 'ditolak'}")
                print("  Hasilnya sama." if nfa_result == dfa_result else "  Ada perbedaan hasil.")
        except ValueError as error:
            print(f"Input tidak valid: {error}")


if __name__ == "__main__":
    main()
