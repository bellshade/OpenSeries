"use client";

import { useNavStyle } from "@/hooks/useNavStyle";
import { ReactNode, useEffect } from "react";

type Props = {
    children: ReactNode;
};

const Layout = ({ children }: Props) => {
    const { setLandingStyles } = useNavStyle();

    useEffect(() => {
        setLandingStyles();
    }, [setLandingStyles]);

    return <>{children}</>;
};

export default Layout;
