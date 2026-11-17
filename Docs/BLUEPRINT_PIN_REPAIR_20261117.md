# BP_Telekinezi pin repair

The reported `CurrentTransaction` ensure occurred during Blueprint compilation alongside `EdGraphPin.cpp` reciprocal-link checks. A compile tool returning normally did not mean the editor log was clean.

Inspected 1,239 nodes across the Blueprint's 60 graphs (3,924 exposed pins). Found one asymmetric connection: UpdateKutGrabFX FunctionEntry_0.then had no outgoing link, while MacroInstance_4.exec still referenced it. This could prevent the grab FX update function from running and triggered compiler link reconciliation ensures.

Repaired that execution connection by clearing both endpoints and reconnecting exactly once. Initial reconnect exposed a duplicate on the input; breaking the now reciprocal link cleared both copies, after which one clean connection was created. No gameplay logic was otherwise changed in this repair.

Two consecutive compiles then succeeded. Checked the fresh log interval after repair: no Ensure, Error, or Warning entries. Saved BP_Telekinezi. In-game behavior was not retested in this repair.

Recovery copy before repair: Backups/BlueprintPinRepair_20261117/BP_Telekinezi.uasset.
