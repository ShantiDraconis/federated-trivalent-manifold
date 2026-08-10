#include <cmath>
#include <iostream>
#include <stdexcept>
#include <string>

struct State {
  double regulator;
  double risk;
  bool quarantined;
};

State step(State s, double epsilon = 1e-6) {
  if (!(epsilon > 0.0)) throw std::invalid_argument("epsilon must be positive");
  const double next = s.regulator + epsilon + s.risk * s.risk;
  if (!std::isfinite(next)) throw std::overflow_error("non-finite state");
  s.regulator = next;
  s.quarantined = s.risk * s.risk > 1.0;
  return s;
}

int main(int argc, char** argv) {
  const double risk = argc > 1 ? std::stod(argv[1]) : 0.2;
  State s{0.0, risk, false};
  const State next = step(s);
  if (!(next.regulator > s.regulator)) return 2;
  std::cout << "{\"runtime\":\"simulator\",\"w\":" << next.regulator
            << ",\"action\":\"" << (next.quarantined ? "QUARANTINE_REQUEST" : "MONITOR")
            << "\",\"dos_immunity_proved\":false}\n";
  return 0;
}
