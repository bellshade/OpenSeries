import type { Config } from "tailwindcss";
import { addDynamicIconSelectors } from "@iconify/tailwind";
import typography from "@tailwindcss/typography";

const config: Config = {
    darkMode: ["class"],
    content: [
        "./components/**/*.{js,ts,jsx,tsx,mdx}",
        "./constants/**/*.{js,ts,jsx,tsx,mdx}",
        "./app/**/*.{js,ts,jsx,tsx,mdx}"
    ],
    theme: {
        extend: {
            container: {
                padding: "2rem",
                center: true
            }
        }
    },
    plugins: [typography(), addDynamicIconSelectors()]
};

export default config;
