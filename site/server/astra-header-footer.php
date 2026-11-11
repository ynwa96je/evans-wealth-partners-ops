// Evans Wealth Partners: Astra header & footer builder configuration.
require_once ABSPATH . 'wp-admin/includes/image.php';
$up   = wp_upload_dir();
$home = trailingslashit( home_url() );
$out  = [];

// ---------- logos (PNG, transparency kept)
$payload = json_decode( file_get_contents( $up['basedir'] . '/ewp-source/payload.json' ), true );
$logo_ids = [];
foreach ( [ 'dark' => 'Evans Wealth Partners logo (dark)', 'light' => 'Evans Wealth Partners logo (light, for navy)' ] as $k => $title ) {
	$dest = $up['path'] . '/ewp-logo-' . $k . '.png';
	file_put_contents( $dest, base64_decode( $payload[ 'logo_' . $k ] ) );
	$aid = wp_insert_attachment( [ 'post_mime_type' => 'image/png', 'post_title' => $title, 'post_status' => 'inherit' ], $dest );
	wp_update_attachment_metadata( $aid, wp_generate_attachment_metadata( $aid, $dest ) );
	update_post_meta( $aid, '_wp_attachment_image_alt', 'Evans Wealth Partners' );
	update_post_meta( $aid, '_ewp_key', 'logo-' . $k );
	$logo_ids[ $k ] = $aid;
}
unlink( $up['basedir'] . '/ewp-source/payload.json' );
set_theme_mod( 'custom_logo', $logo_ids['dark'] );
update_option( 'blogname', 'Evans Wealth Partners' );
update_option( 'blogdescription', 'Family wealth management' );
$out['logos'] = $logo_ids;

// ---------- primary menu
$menu = wp_get_nav_menu_object( 'Primary' );
$menu_id = $menu ? $menu->term_id : wp_create_nav_menu( 'Primary' );
foreach ( wp_get_nav_menu_items( $menu_id ) ?: [] as $item ) { wp_delete_post( $item->ID, true ); }
$pos = 1;
foreach ( [ 84 => 'Home', 129 => 'About', 154 => 'Services', 176 => 'Resources', 194 => 'Contact' ] as $pid => $label ) {
	wp_update_nav_menu_item( $menu_id, 0, [ 'menu-item-title' => $label, 'menu-item-object' => 'page', 'menu-item-object-id' => $pid, 'menu-item-type' => 'post_type', 'menu-item-status' => 'publish', 'menu-item-position' => $pos++ ] );
}
$locations = get_theme_mod( 'nav_menu_locations', [] );
$locations['primary']     = $menu_id;
$locations['mobile_menu'] = $menu_id;
set_theme_mod( 'nav_menu_locations', $locations );
$out['menu'] = $menu_id;

// ---------- helpers
$c   = fn( $i ) => 'var(--ast-global-color-' . $i . ')';
$r3  = fn( $d, $t = null, $m = null ) => [ 'desktop' => $d, 'tablet' => $t ?? '', 'mobile' => $m ?? '' ];
$fs  = fn( $d, $t = '', $m = '' ) => [ 'desktop' => $d, 'tablet' => $t, 'mobile' => $m, 'desktop-unit' => 'px', 'tablet-unit' => 'px', 'mobile-unit' => 'px' ];
$box = fn( $t, $r, $b, $l ) => [ 'top' => $t, 'right' => $r, 'bottom' => $b, 'left' => $l ];
$sp  = fn( $d, $t = null, $m = null ) => [ 'desktop' => $d, 'tablet' => $t ?? [ 'top' => '', 'right' => '', 'bottom' => '', 'left' => '' ], 'mobile' => $m ?? [ 'top' => '', 'right' => '', 'bottom' => '', 'left' => '' ], 'desktop-unit' => 'px', 'tablet-unit' => 'px', 'mobile-unit' => 'px' ];
$bg  = function ( $color ) {
	$one = [ 'background-color' => $color, 'background-image' => '', 'background-repeat' => 'repeat', 'background-position' => 'center center', 'background-size' => 'auto', 'background-attachment' => 'scroll', 'overlay-type' => '', 'overlay-color' => '', 'overlay-opacity' => '', 'overlay-gradient' => '' ];
	$none = array_merge( $one, [ 'background-color' => '' ] );
	return [ 'desktop' => $one, 'tablet' => $none, 'mobile' => $none ];
};
$extras = fn( $lh, $lh_unit = '', $ls = '', $tt = '' ) => [ 'line-height' => $lh, 'line-height-unit' => $lh_unit, 'letter-spacing' => $ls, 'letter-spacing-unit' => 'px', 'text-transform' => $tt, 'text-decoration' => '' ];
$SANS  = "'Source Sans 3', sans-serif";
$SERIF = "'Source Serif 4', serif";
$muted = '#C5CDD6'; $on_navy = '#F7F5F0'; $navy_line = '#2E4A68'; $slate_muted = '#5E6873';

$opts = [];

// ---------- global palette, fonts, buttons
$palette = astra_get_option( 'global-color-palette' );
// 0 brand(pitch) 1 brand hover 2 headings(navy) 3 text(slate) 4 white 5 paper 6 navy 7 line 8 brass
$palette['palette'] = [ '#1F6B4A', '#17573C', '#13263A', '#3E4A56', '#FFFFFF', '#F7F5F0', '#13263A', '#DDD7CB', '#B08D57' ];
$opts['global-color-palette'] = $palette;
$opts['body-font-family']     = $SANS;
$opts['body-font-variant']    = '400';
$opts['body-font-weight']     = '400';
$opts['font-size-body']       = $fs( 17 );
$opts['body-font-extras']     = $extras( '1.65' );
$opts['headings-font-family'] = $SERIF;
$opts['headings-font-weight'] = '600';
$opts['headings-font-variant'] = '600';
$opts['button-color']         = $c( 4 );
$opts['button-h-color']       = $c( 4 );
$opts['button-bg-color']      = $c( 0 );
$opts['button-bg-h-color']    = $c( 1 );
$opts['theme-button-padding'] = $sp( $box( 12, 24, 12, 24 ), $box( 12, 24, 12, 24 ), $box( 12, 24, 12, 24 ) );
$opts['button-radius-fields'] = $sp( $box( 4, 4, 4, 4 ), $box( 4, 4, 4, 4 ), $box( 4, 4, 4, 4 ) );
$opts['font-family-button']   = $SANS;
$opts['font-weight-button']   = '600';
$opts['font-size-button']     = $fs( 16 );
$opts['font-extras-button']   = $extras( '1.25', '' );
$opts['theme-button-border-group-border-size']    = $box( 1, 1, 1, 1 );
$opts['theme-button-border-group-border-color']   = $c( 0 );
$opts['theme-button-border-group-border-h-color'] = $c( 1 );

// ---------- site identity: logo image only
$opts['display-site-title-responsive']   = [ 'desktop' => 0, 'tablet' => 0, 'mobile' => 0 ];
$opts['display-site-tagline-responsive'] = [ 'desktop' => 0, 'tablet' => 0, 'mobile' => 0 ];
$opts['ast-header-responsive-logo-width'] = [ 'desktop' => 222, 'tablet' => 222, 'mobile' => 202 ];

// ---------- header layout
$opts['mobile-header-breakpoint'] = 767;
$opts['header-desktop-items'] = [
	'popup'   => [ 'popup_content' => [ 'mobile-menu', 'button-1' ] ],
	'above'   => [ 'above_left' => [], 'above_left_center' => [], 'above_center' => [], 'above_right_center' => [], 'above_right' => [] ],
	'primary' => [ 'primary_left' => [ 'logo' ], 'primary_left_center' => [], 'primary_center' => [], 'primary_right_center' => [], 'primary_right' => [ 'menu-1', 'button-1' ] ],
	'below'   => [ 'below_left' => [], 'below_left_center' => [], 'below_center' => [], 'below_right_center' => [], 'below_right' => [] ],
];
$opts['header-mobile-items'] = [
	'popup'   => [ 'popup_content' => [ 'mobile-menu', 'button-1' ] ],
	'above'   => [ 'above_left' => [], 'above_center' => [], 'above_right' => [] ],
	'primary' => [ 'primary_left' => [ 'logo' ], 'primary_center' => [], 'primary_right' => [ 'mobile-trigger' ] ],
	'below'   => [ 'below_left' => [], 'below_center' => [], 'below_right' => [] ],
];
$opts['hb-header-height']            = [ 'desktop' => 82, 'tablet' => 82, 'mobile' => 70 ];
$opts['hb-header-main-sep']          = 1;
$opts['hb-header-main-sep-color']    = $c( 7 );
$opts['hb-header-bg-obj-responsive'] = $bg( $c( 4 ) );
$opts['hb-header-main-layout-width'] = 'content';

// menu 1
$opts['header-menu1-font-family']        = $SANS;
$opts['header-menu1-font-weight']        = '600';
$opts['header-menu1-font-size']          = $fs( 16 );
$opts['header-menu1-font-extras']        = $extras( '1.25', '' );
$opts['header-menu1-color-responsive']   = $r3( $c( 3 ), $c( 3 ) );
$opts['header-menu1-h-color-responsive'] = $r3( $c( 2 ), $c( 2 ) );
$opts['header-menu1-a-color-responsive'] = $r3( $c( 2 ), $c( 2 ) );
$opts['header-menu1-menu-spacing']       = $sp( $box( 12, 16, 12, 16 ), $box( 12, 12, 12, 12 ) );
$opts['header-menu1-menu-hover-animation'] = '';

// button 1 (the header CTA; hidden on tablet as in the design)
$opts['header-button1-text']          = 'Book an intro call';
$opts['header-button1-link-option']   = [ 'url' => $home . 'contact/', 'new_tab' => false, 'link_rel' => '' ];
$opts['header-button1-font-family']   = $SANS;
$opts['header-button1-font-weight']   = '600';
$opts['header-button1-font-size']     = $fs( 16 );
$opts['header-button1-font-extras']   = $extras( '1.25', '' );
$opts['header-button1-back-color']    = $r3( $c( 0 ) );
$opts['header-button1-text-color']    = $r3( $c( 4 ) );
$opts['header-button1-back-h-color']  = $r3( $c( 1 ) );
$opts['header-button1-text-h-color']  = $r3( $c( 4 ) );
$opts['header-button1-border-color']  = $r3( $c( 0 ) );
$opts['header-button1-border-h-color'] = $r3( $c( 1 ) );
$opts['header-button1-border-size']   = $box( 1, 1, 1, 1 );
$opts['header-button1-border-radius-fields'] = $sp( $box( 4, 4, 4, 4 ), $box( 4, 4, 4, 4 ), $box( 4, 4, 4, 4 ) );
$opts['section-hb-button-1-padding']  = $sp( $box( 12, 24, 12, 24 ), $box( 12, 24, 12, 24 ), $box( 12, 24, 12, 24 ) );
$opts['section-hb-button-1-visibility-responsive'] = [ 'desktop' => 1, 'tablet' => 0, 'mobile' => 1 ];

// mobile trigger: outlined "Menu" button
$opts['header-trigger-icon']                     = 'menu';
$opts['mobile-header-toggle-btn-style']          = 'outline';
$opts['mobile-header-menu-label']                = 'Menu';
$opts['mobile-header-toggle-btn-color']          = $c( 2 );
$opts['mobile-header-toggle-border-color']       = $slate_muted;
$opts['mobile-header-toggle-btn-border-size']    = $box( 1, 1, 1, 1 );
$opts['mobile-header-toggle-border-radius-fields'] = $sp( $box( 4, 4, 4, 4 ), $box( 4, 4, 4, 4 ), $box( 4, 4, 4, 4 ) );
$opts['mobile-header-label-font-size']           = 16;
$opts['mobile-header-toggle-icon-size']          = 20;

// mobile menu: large serif links with a hairline between items
$opts['mobile-header-type']                    = 'dropdown';
$opts['header-mobile-menu-font-family']        = $SERIF;
$opts['header-mobile-menu-font-weight']        = '600';
$opts['header-mobile-menu-font-size']          = $fs( 22, 22, 22 );
$opts['header-mobile-menu-color-responsive']   = $r3( $c( 2 ), $c( 2 ), $c( 2 ) );
$opts['header-mobile-menu-h-color-responsive'] = $r3( $c( 0 ), $c( 0 ), $c( 0 ) );
$opts['header-mobile-menu-a-color-responsive'] = $r3( $c( 0 ), $c( 0 ), $c( 0 ) );
$opts['header-mobile-menu-bg-obj-responsive']  = [ 'desktop' => $bg( $c( 4 ) )['desktop'], 'tablet' => $bg( $c( 4 ) )['desktop'], 'mobile' => $bg( $c( 4 ) )['desktop'] ];
$opts['header-mobile-menu-submenu-item-border'] = true;
$opts['header-mobile-menu-submenu-item-b-size'] = '1';
$opts['header-mobile-menu-submenu-item-b-color'] = $c( 7 );
$opts['header-mobile-menu-menu-spacing']       = $sp( $box( 16, 0, 16, 0 ), $box( 16, 0, 16, 0 ), $box( 16, 0, 16, 0 ) );

// ---------- footer layout: above = brand + 3 link columns, primary = disclosure, below = meta
$opts['footer-desktop-items'] = [
	'above'   => [ 'above_1' => [ 'widget-1' ], 'above_2' => [ 'widget-2' ], 'above_3' => [ 'widget-3' ], 'above_4' => [ 'widget-4' ], 'above_5' => [] ],
	'primary' => [ 'primary_1' => [ 'html-1' ], 'primary_2' => [], 'primary_3' => [], 'primary_4' => [], 'primary_5' => [] ],
	'below'   => [ 'below_1' => [ 'copyright' ], 'below_2' => [ 'html-2' ], 'below_3' => [], 'below_4' => [], 'below_5' => [] ],
];
// above row
$opts['hba-footer-column']            = '4';
$opts['hba-footer-layout']            = [ 'desktop' => '4-lheavy', 'tablet' => '2-equal', 'mobile' => 'full' ];
$opts['hba-inner-spacing']            = [ 'desktop' => 48, 'tablet' => 32, 'mobile' => 32 ];
$opts['hba-footer-bg-obj-responsive'] = $bg( $c( 6 ) );
$opts['hba-footer-separator']         = 0;
$opts['hba-footer-height']            = '';
$opts['hba-footer-layout-width']      = 'content';
$opts['hba-footer-vertical-alignment'] = 'flex-start';
$opts['section-above-footer-builder-padding'] = $sp( $box( 64, '', 48, '' ), $box( 64, '', 48, '' ), $box( 48, '', 32, '' ) );
// primary row (disclosure) with the navy hairline on top
$opts['hb-footer-column']             = '1';
$opts['hb-footer-layout']             = [ 'desktop' => 'full', 'tablet' => 'full', 'mobile' => 'full' ];
$opts['hb-footer-bg-obj-responsive']  = $bg( $c( 6 ) );
$opts['hb-footer-main-sep']           = 1;
$opts['hb-footer-main-sep-color']     = $navy_line;
$opts['hb-primary-footer-height']     = '';
$opts['hb-footer-layout-width']       = 'content';
$opts['section-primary-footer-builder-padding'] = $sp( $box( 32, '', 16, '' ), $box( 32, '', 16, '' ), $box( 32, '', 16, '' ) );
// below row (copyright + place)
$opts['hbb-footer-column']            = '2';
$opts['hbb-footer-layout']            = [ 'desktop' => '2-equal', 'tablet' => '2-equal', 'mobile' => 'full' ];
$opts['hbb-inner-spacing']            = [ 'desktop' => 16, 'tablet' => 16, 'mobile' => 8 ];
$opts['hbb-footer-bg-obj-responsive'] = $bg( $c( 6 ) );
$opts['hbb-footer-separator']         = 0;
$opts['hbb-footer-height']            = '';
$opts['hbb-footer-layout-width']      = 'content';
$opts['hbb-footer-vertical-alignment'] = 'flex-start';
$opts['section-below-footer-builder-padding'] = $sp( $box( 0, '', 40, '' ), $box( 0, '', 40, '' ), $box( 0, '', 32, '' ) );

// copyright + html elements
$opts['footer-copyright-editor']             = '© [current_year] Evans Wealth Partners';
$opts['footer-copyright-color']              = $muted;
$opts['font-size-section-footer-copyright']  = $fs( 15 );
$opts['footer-copyright-alignment']          = [ 'desktop' => 'left', 'tablet' => 'left', 'mobile' => 'left' ];
$opts['footer-html-1'] = '<p>Evans Wealth Partners provides financial planning and wealth management to families and business owners. The information on this website is general and educational. It is not personal investment, tax or legal advice. Investing involves risk, including the possible loss of principal, and past performance does not guarantee future results.</p>';
$opts['footer-html-1color']                  = $r3( $muted );
$opts['font-size-section-fb-html-1']         = $fs( 15 );
$opts['footer-html-1-alignment']             = [ 'desktop' => 'left', 'tablet' => 'left', 'mobile' => 'left' ];
$opts['footer-html-2']                       = '<p>Avon, Connecticut</p>';
$opts['footer-html-2color']                  = $r3( $muted );
$opts['font-size-section-fb-html-2']         = $fs( 15 );
$opts['footer-html-2-alignment']             = [ 'desktop' => 'right', 'tablet' => 'right', 'mobile' => 'left' ];

// footer widget colours and sizes
foreach ( [ 1, 2, 3, 4 ] as $i ) {
	$opts[ "footer-widget-$i-title-color" ]       = $r3( $c( 8 ) );
	$opts[ "footer-widget-$i-color" ]             = $r3( $i === 1 ? $muted : $on_navy );
	$opts[ "footer-widget-$i-link-color" ]        = $r3( $on_navy );
	$opts[ "footer-widget-$i-link-h-color" ]      = $r3( $on_navy );
	$opts[ "footer-widget-$i-content-font-size" ] = $fs( 17 );
	$opts[ "footer-widget-alignment-$i" ]         = [ 'desktop' => 'left', 'tablet' => 'left', 'mobile' => 'left' ];
}

foreach ( $opts as $k => $v ) { astra_update_option( $k, $v ); }
$out['options_written'] = count( $opts );

// ---------- footer widget blocks
$title = fn( $t ) => '<!-- wp:paragraph {"style":{"typography":{"fontSize":"13px","fontWeight":"600","letterSpacing":"0.14em","textTransform":"uppercase","lineHeight":"1.25"},"color":{"text":"#b08d57"}}} --><p class="has-text-color" style="color:#b08d57;font-size:13px;font-weight:600;letter-spacing:0.14em;line-height:1.25;text-transform:uppercase">' . esc_html( $t ) . '</p><!-- /wp:paragraph -->';
$nav = function ( $links ) {
	$inner = '';
	foreach ( $links as $label => $url ) {
		$inner .= '<!-- wp:navigation-link ' . wp_json_encode( [ 'label' => $label, 'url' => $url, 'kind' => 'custom', 'isTopLevelLink' => true ] ) . ' /-->';
	}
	return '<!-- wp:navigation {"overlayMenu":"never","layout":{"type":"flex","orientation":"vertical"},"style":{"spacing":{"blockGap":"20px"},"typography":{"fontSize":"17px"}}} -->' . $inner . '<!-- /wp:navigation -->';
};
$group = fn( $inner, $gap ) => '<!-- wp:group {"style":{"spacing":{"blockGap":"' . $gap . '"}},"layout":{"type":"flex","orientation":"vertical","justifyContent":"left"}} --><div class="wp-block-group">' . $inner . '</div><!-- /wp:group -->';
$logo_light_url = wp_get_attachment_url( $logo_ids['light'] );
$w1 = $group(
	'<!-- wp:image {"id":' . $logo_ids['light'] . ',"width":"222px","sizeSlug":"full","linkDestination":"custom"} --><figure class="wp-block-image size-full is-resized"><a href="' . esc_url( $home ) . '"><img src="' . esc_url( $logo_light_url ) . '" alt="Evans Wealth Partners" class="wp-image-' . $logo_ids['light'] . '" style="width:222px"/></a></figure><!-- /wp:image -->'
	. '<!-- wp:paragraph --><p>A family-run wealth management firm based in Avon, working with families and businesses across Connecticut and beyond. We write the plan first, then manage the money around it.</p><!-- /wp:paragraph -->'
	. '<!-- wp:buttons --><div class="wp-block-buttons"><!-- wp:button --><div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="' . esc_url( $home . 'contact/' ) . '">Book an intro call</a></div><!-- /wp:button --></div><!-- /wp:buttons -->',
	'24px'
);
$w2 = $group( $title( 'Pages' ) . $nav( [ 'Home' => $home, 'About' => $home . 'about/', 'Services' => $home . 'services/', 'Resources' => $home . 'resources/', 'Contact' => $home . 'contact/' ] ), '16px' );
$w3 = $group( $title( 'Services' ) . $nav( [
	'Financial planning' => $home . 'services/#planning', 'Retirement planning' => $home . 'services/#retirement', 'Investments' => $home . 'services/#investments',
	'Protection strategies' => $home . 'services/#protection', 'Income strategies' => $home . 'services/#income', 'Estate planning' => $home . 'services/#estate',
	'Business planning' => $home . 'services/#business-planning' ] ), '16px' );
$detail = fn( $t ) => '<!-- wp:paragraph {"style":{"typography":{"fontSize":"15px"},"color":{"text":"#c5cdd6"}}} --><p class="has-text-color" style="color:#c5cdd6;font-size:15px">' . esc_html( $t ) . '</p><!-- /wp:paragraph -->';
$w4 = $group( $title( 'Get in touch' ) . $nav( [ 'john@evanswealthpartners.com' => 'mailto:john@evanswealthpartners.com' ] )
	. $detail( 'Avon, the Farmington Valley, Connecticut and beyond.' ) . $detail( 'Meetings at your home, your business or virtually.' ), '16px' );

$wb = get_option( 'widget_block', [ '_multiwidget' => 1 ] );
$sw = get_option( 'sidebars_widgets', [] );
$next = max( array_filter( array_keys( $wb ), 'is_int' ) ?: [ 1 ] ) + 1;
foreach ( [ 1 => $w1, 2 => $w2, 3 => $w3, 4 => $w4 ] as $i => $content ) {
	// replace anything previously placed in these areas
	foreach ( $sw[ "footer-widget-$i" ] ?? [] as $wid ) { if ( preg_match( '/^block-(\d+)$/', $wid, $m ) ) unset( $wb[ (int) $m[1] ] ); }
	$wb[ $next ] = [ 'content' => $content ];
	$sw[ "footer-widget-$i" ] = [ 'block-' . $next ];
	$next++;
}
update_option( 'widget_block', $wb );
update_option( 'sidebars_widgets', $sw );
$out['widgets'] = array_intersect_key( $sw, array_flip( [ 'footer-widget-1', 'footer-widget-2', 'footer-widget-3', 'footer-widget-4' ] ) );

// ---------- refresh generated CSS and caches
do_action( 'astra_ability_settings_updated', 'ewp/header-footer', [] );
if ( class_exists( 'Astra_Cache_Base' ) ) { do_action( 'astra_post_meta_updated' ); }
delete_option( 'astra-theme-dynamic-css' );
if ( function_exists( 'astra_clear_all_assets_cache' ) ) { astra_clear_all_assets_cache(); }
\Elementor\Plugin::$instance->files_manager->clear_cache();
wp_set_current_user( 1 );
$purge = rest_do_request( new WP_REST_Request( 'DELETE', '/hostinger-tools-plugin/v1/clear-cache' ) );
$out['purge'] = $purge->get_data()['data']['message'] ?? $purge->get_data();
return $out;
