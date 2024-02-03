import remarkGfm from "remark-gfm";
import createMDX from "@next/mdx";
import rehypePrettyCode from "rehype-pretty-code";

/** @type {import('next').NextConfig} */
const nextConfig = {
    pageExtensions: ["js", "jsx", "mdx", "md", "ts", "tsx"]
};

const options = {
    theme: {
        light: "light-plus",
        dark: "dark-plus"
    }
};

const withMDX = createMDX({
    options: {
        remarkPlugins: [remarkGfm],
        rehypePlugins: [[rehypePrettyCode, options]]
    }
});

export default withMDX(nextConfig);
