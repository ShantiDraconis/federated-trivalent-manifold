namespace FTM.Renormalization

/-- Integer-scaled boundary drift: -(a*e+b), with a=21774 and b=1000. -/
def driftScaled (e : Nat) : Int :=
  -Int.ofNat (21774 * e + 1000)

theorem drift_strictly_negative (e : Nat) : driftScaled e < 0 := by
  unfold driftScaled
  omega

/-- A positive constant subtraction does not establish convergence to zero. -/
def equilibriumScaled : Int := -1000

theorem equilibriumScaled_negative : equilibriumScaled < 0 := by decide

end FTM.Renormalization
