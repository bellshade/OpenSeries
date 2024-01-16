import { glob } from "glob";

export const allDocs = async () => {
    return await glob("**/page.mdx", { cwd: process.cwd() + "/app/docs" });
};
