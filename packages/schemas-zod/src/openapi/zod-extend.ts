/**
 * Side-effect: extend the global Zod module with .openapi() so that when the OpenAPI
 * generator runs, any schema created with `import z from "zod"` has .openapi().
 * Import this first in generate-openapi.ts before loading any schemas.
 */
import { extendZodWithOpenApi } from "@asteasolutions/zod-to-openapi";
import * as z from "zod";

extendZodWithOpenApi(z);
