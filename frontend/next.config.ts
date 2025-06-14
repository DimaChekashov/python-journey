import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  reactStrictMode: true,
  pageExtensions: ["page.jsx", "page.tsx", "page.js", "page.jsx"],
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
