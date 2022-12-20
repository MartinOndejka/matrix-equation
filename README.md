# Iterative methods for matrix equations solving

## Running

```bash
pip install -r requirements.txt
python main.py
```

## Output

```bash
ro=0.19776616524502583
Jacobi converged in 8 iterations for gamma=10
ro=0.03911145611572259
Gauss-Seidel converged in 6 iterations for gamma=10
ro=0.9888308262251283
Jacobi converged in 986 iterations for gamma=2
ro=0.9777864028930694
Gauss-Seidel converged in 494 iterations for gamma=2
ro=2.4720770655628215
Jacobi did not converge for gamma=0.8
ro=6.111165018081659
Gauss-Seidel did not converge for gamma=0.8
```

## Jacobiho metoda

Pre `γ = 10` ma matica `W = E - D^-1 * A` spektralny polomer ~ 0.20 => mala by konvergovat, co zodpoveda najedenemu vysledku.

Pre `γ = 2` ma matica `W = E - D^-1 * A` spektralny polomer ~ 0.99 => mala by konvergovat, co zodpoveda najedenemu vysledku.

Pre `γ = 0.8` ma matica `W = E - D^-1 * A` spektralny polomer ~ 2.47 => nemala by konvergovat, co zodpoveda najedenemu vysledku.

## Gauss-Seidelova metoda

Pre `γ = 10` ma matica `W = E - D^-1 * A` spektralny polomer ~ 0.04 => mala by konvergovat, co zodpoveda najedenemu vysledku.

Pre `γ = 2` ma matica `W = E - D^-1 * A` spektralny polomer ~ 0.98 => mala by konvergovat, co zodpoveda najedenemu vysledku.

Pre `γ = 0.8` ma matica `W = E - D^-1 * A` spektralny polomer ~ 6.11 => nemala by konvergovat, co zodpoveda najedenemu vysledku.
